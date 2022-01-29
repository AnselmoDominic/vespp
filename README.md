# VESPP
Very Extraordinarily Simple Python Proxy

VESPP is built to be a Python TCP proxy that's easy to digest at a quick glance of the code. 
It's function is to simply be a man-in-the-middle, take TCP traffic from one end and forward it out to the other end.
A possible use case of this script would be if you wanted to use packet capture software to see what a device is doing. E.g. a printer scan-to-email that won't play nice with your mail server. 

### Usage
Simply run vespp.py with Python 3. 
First it will ask for the remote server. This is where all your traffic should end up.
Then it will ask for the listen port. This is the port the proxy will listen on.
If you get an Access Denied error at this step, use a higher port number. 
Lastly, it will ask for the remote port. This is the port the remote server is listening at.

Once all that is done, the server will start. All you have to do now is connect to it and your traffic will be forwarded off. 
