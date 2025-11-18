Remote Command Executor

This project allows you to execute authorized, remote administrative commands on your own system using Python and Flask.
It is intended only for personal labs, automation, and ethical testing.
Never use this on systems you do not own or have permission to manage.

✅ Requirements

Before running the project, make sure you have:

Python 3.x

Flask installed

pip install flask


A public IP address (optional if using a tunneling service like ngrok)

Port 5000 allowed in your firewall (if using your own IP)

🌐 Optional: Use a Free Hosting/Tunneling Service (e.g., ngrok)

If you don’t have a public IP or port-forwarding capability, you can expose your Flask server using ngrok or similar services.

How to use ngrok:

Download ngrok from their official website

Start your Flask server:

python3 app.py


Run ngrok to expose port 5000:

ngrok http 5000


ngrok will give you a public HTTPS URL like:

https://random-subdomain.ngrok.io


Use that URL to access the remote command interface.

⚙️ Running the Server (Direct Method)

If using your own IP:

Start the Python script:

python3 app.py


Then access it remotely through:

http://YOUR_PUBLIC_IP:5000

🔐 Important Security Note

Before using the tool, change the default password inside the Python code.

The current default password is:

P@S5worD


Edit the script and set your own strong password such as:

MyStr0ng!Pass2025

⚠️ Disclaimer

This tool is for educational, testing, and personal system administration only.
Unauthorized use on systems you do not own may be illegal. Use responsibly.
