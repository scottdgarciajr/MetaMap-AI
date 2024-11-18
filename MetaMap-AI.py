import subprocess
import xml.etree.ElementTree as ET
import openai
import json

# OpenAI API Key
openai.api_key = "your-openai-api-key"

def run_nmap(target, options="-T4 -sV"):
    """Run Nmap scan and save output to XML."""
    print("[*] Running Nmap...")
    output_file = "nmap_output.xml"
    command = f"nmap {options} {target} -oX {output_file}"
    subprocess.run(command, shell=True)
    print(f"[+] Scan complete. Results saved to {output_file}")
    return output_file

def parse_nmap_output(file):
    """Parse Nmap XML output for hosts, ports, and services."""
    print("[*] Parsing Nmap results...")
    tree = ET.parse(file)
    root = tree.getroot()
    parsed_results = []

    for host in root.findall("host"):
        ip = host.find("address").get("addr")
        ports = []
        for port in host.findall(".//port"):
            port_id = port.get("portid")
            service = port.find("service").get("name")
            version = port.find("service").get("version", "unknown")
            ports.append({"port": port_id, "service": service, "version": version})
        parsed_results.append({"ip": ip, "ports": ports})

    print(f"[+] Parsed {len(parsed_results)} hosts.")
    return parsed_results

def generate_metasploit_commands(scan_results):
    """Generate Metasploit commands using OpenAI."""
    print("[*] Generating Metasploit commands...")
    prompt = f"""
    Based on these Nmap results, suggest Metasploit modules and commands:
    {json.dumps(scan_results, indent=2)}
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.7,
    )
    commands = response.choices[0].text.strip()
    print("[+] Metasploit commands generated.")
    return commands

def execute_metasploit(commands):
    """Execute Metasploit commands via a resource script."""
    print("[*] Writing Metasploit resource script...")
    resource_file = "metasploit_script.rc"
    with open(resource_file, "w") as file:
        file.write(commands)

    print("[*] Running Metasploit...")
    command = f"msfconsole -r {resource_file}"
    subprocess.run(command, shell=True)

def main():
    print("Welcome to MetaMap AI!")
    print("=======================")

    # Step 1: Get user input for Nmap scan
    target = input("Enter target IP or range: ").strip()
    nmap_options = input("Enter Nmap options (default: -T4 -sV): ").strip() or "-T4 -sV"

    # Step 2: Run Nmap and parse results
    nmap_file = run_nmap(target, nmap_options)
    scan_results = parse_nmap_output(nmap_file)

    # Step 3: Generate Metasploit commands
    metasploit_commands = generate_metasploit_commands(scan_results)
    print("\nSuggested Metasploit Commands:")
    print("==============================")
    print(metasploit_commands)

    # Step 4: Execute Metasploit
    execute_now = input("\nDo you want to execute these commands? (yes/no): ").strip().lower()
    if execute_now == "yes":
        execute_metasploit(metasploit_commands)
    else:
        print("[*] Metasploit execution skipped.")

if __name__ == "__main__":
    main()
