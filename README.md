# **MetaMap AI**

MetaMap AI is a Python-based tool that combines the power of **Nmap**, **Metasploit**, and **Generative AI** to automate vulnerability detection and exploitation. With a simple CLI, MetaMap AI analyzes Nmap scan results and uses AI to suggest Metasploit commands, providing a streamlined workflow for penetration testing.

---

## **Features**
- 🛠️ **Nmap Integration**: Perform network scans with customizable options.
- 🤖 **Generative AI Suggestions**: Use AI to analyze scan results and recommend Metasploit modules and commands.
- 🚀 **Metasploit Automation**: Automate Metasploit command execution via resource scripts.
- 🔍 **Results Parsing**: Parse and display Nmap results for easy interpretation.
- 💻 **Command-Line Interface (CLI)**: Simple, interactive UI for controlling the tool.

---

## **How It Works**
1. **Nmap Scanning**:  
   Input a target IP/range and scan preferences. MetaMap runs Nmap and saves the results.
   
2. **AI Analysis**:  
   Nmap results are parsed and sent to an AI model, which suggests appropriate Metasploit commands.

3. **Metasploit Execution**:  
   Execute the AI-suggested commands in Metasploit to test for vulnerabilities.

4. **Output & Logs**:  
   Display scan results, AI suggestions, and Metasploit execution logs.

---

## **Installation**

### **Prerequisites**
- **Python 3.8+**
- **Nmap**: Install with `sudo apt install nmap` or your OS package manager.
- **Metasploit**: Install via [Metasploit Framework](https://www.metasploit.com/).
- **OpenAI API Key**: Obtain from [OpenAI](https://openai.com/api/).

### **Setup**
1. Clone the repository:
   ```bash
   git clone https://github.com/scottdgarciajr/MetaMap-AI.git
   cd MetaMap-AI
2. Install dependencies:
bash
Copy code
pip install -r requirements.txt
3. Set your OpenAI API key:
Open metamap_ai.py.
Replace "your-openai-api-key" with your actual API key.
### **Usage**

**Run MetaMap AI**
bash
Copy code
python metamap_ai.py
**Workflow**
Input Target:
Enter the target IP/range and optional Nmap scan options (default: -T4 -sV).
Review Results:
View parsed Nmap results and AI-suggested Metasploit commands.
Execute Commands:
Optionally execute Metasploit commands or save them for manual use.
