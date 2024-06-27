# Quick Message
Source code for [this blog post](https://zainj.dev/posts?post=building-a-textbased-messaging-platform) about building a multi-person messaging platform using web sockets.

## Setup
Start by cloning this repository:

```
git clone https://github.com/zainmfjavaid/QuickMessage
```

Then, install the package requirements by running:

```
pip install -r requirements.txt
```

Although not strictly required, it might also be a good idea to set your Flask secret key to something secure. You can find this field in the **app.py** file on line 6:

```
app.secret_key = '<replace_with_secret_key>'
```

## Running/Accessing the App
You can start the chat app by running the **app.py** file.

If you'd like to chat with other people, ensure they are connected to the same WiFi network as the hosted server and provide them with the server's local network IP address instead of the loopback address (127.0.0.1). The local network IP address should be the last one listed when you first start the server.