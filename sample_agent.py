# Dependencies - > "pip install phi groq python-dotenv"
#  Run this on your Powershell terminal
# Steps
# 1. search Powershell --> then right click on Windows Powershell
# 2. and run the code "Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned"
# 3. when Prompted type "Y" and press "Enter"

# Also set the path -> run this on terminal or your_own_file_path ( cd "C:\Users\Subham Gupta\Desktop\Work\Ai_agents")


try:
    from phi.agent import Agent
    from phi.model.groq import Groq
    from dotenv import load_dotenv
    import os

    # Load environment variables
    # load_dotenv()
    os.environ["GROQ_API_KEY"] = "your_api_key"

    from groq import Client
    client = Client()

    agent = Agent(model=Groq(id="llama-3.3-70b-versatile"))

    # Generate a response
    response = agent.print_response("Write a comparison between momo and tea")
    print(response)

except Exception as e:
    print(f"An error occurred: {e}")


