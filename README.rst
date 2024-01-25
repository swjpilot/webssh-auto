WebSSHAuto
------

Introduction
~~~~~~~~~~~~

 simple web application to be used as an ssh client to connect 
 to your ssh servers. It is written in Python, base on tornado, 
 paramiko and xterm.js.  This implementation has options on the 
 commandline to force login to a specific SSH server using a 
 specific user if you would like upon load of the webpage.


Features
~~~~~~~~

-  SSH password authentication supported, including empty password.
-  SSH public-key authentication supported, including DSA RSA ECDSA
   Ed25519 keys.
-  Encrypted keys supported.
-  Two-Factor Authentication (time-based one-time password) supported.
-  Fullscreen terminal supported.
-  Terminal window resizable.
-  Auto detect the ssh server's default encoding.
-  Modern browsers including Chrome, Firefox, Safari, Edge, Opera
   supported.
-  Can be set to autoconnect to a ssh server with options from command line
   

Preview
~~~~~~~

|Login| |Terminal|

How it works
~~~~~~~~~~~~

::

    +---------+     http     +--------+    ssh    +-----------+
    | browser | <==========> | webssh | <=======> | ssh server|
    +---------+   websocket  +--------+    ssh    +-----------+

Requirements
~~~~~~~~~~~~

-  Python 3.8+

Quickstart
~~~~~~~~~~

1. Install this app, run command ``pip install git+https://github.com/swjpilot/websshauto.git``
2. Start a webserver, run command ``wsshauto``
3. Open your browser, navigate to ``127.0.0.1:8888``
4. Input your data, submit the form.

Server options
~~~~~~~~~~~~~~
.. code:: options

    Usage: /usr/local/bin/wsshauto [OPTIONS]

    Options:

    --help                           show this help information

    /usr/local/lib/python3.9/site-packages/websshauto/settings.py options:

    --address                        Listen address

    --autoconnect                    Auto Connect to SSH Server (default false)

    --bgcolor                        Terminal Background color (default black)

    --certfile                       SSL certificate file

    --curcolor                       Terminal Cursor Color (default white)

    --debug                          Debug mode (default False)

    --delay                          The delay to call recycle_worker (default 3)

    --encoding                       The default character encoding of ssh
                                    servers. Example: --encoding='utf-8' to
                                    solve the problem with some switches&routers

    --fbidhttp                       Forbid public plain http incoming requests                                  
                                    (default True)
    
    --fgcolor                        Terminal Text Color (default white)

    --font                           custom font filename
    
    --hostfile                       User defined host keys file
    
    --keyfile                        SSL private key file
    
    --maxconn                        Maximum live connections (ssh sessions) per
                                    client (default 20)
    
    --origin                         Origin policy, 'same': same origin policy,
                                    matches host name and port number;
                                    'primary': primary domain policy, matches
                                    primary domain only; '<domains>': custom
                                    domains policy, matches any domain in the
                                    <domains> list separated by comma; '*':
                                    wildcard policy, matches any domain, allowed
                                    in debug mode only. (default same)
    
    --password                       password to use to connect automatically
    
    --policy                         Missing host key policy,
                                    reject|autoadd|warning (default warning)
    
    --port                           Listen port (default 8888)
    
    --redirect                       Redirecting http to https (default True)
    
    --sshhost                        hostname to connect to automatically
    
    --sshport                        hostname to connect to automatically
                                    (default 22)
    
    --ssladdress                     SSL listen address
    
    --sslport                        SSL listen port (default 4433)
    
    --syshostfile                    System wide host keys file
    
    --tdstream                       Trusted downstream, separated by comma
    
    --term                           emulation to use to connect automatically
    
    --timeout                        SSH connection timeout (default 3)
    
    --user                           user to use to connect automatically
    
    --version                        Show version information
    
    --wpintvl                        Websocket ping interval (default 0)
    
    --xheaders                       Support xheaders (default True)
    
    --xsrf                           CSRF protection (default True)

    --log-file-max-size              max size of log files before rollover
                                    (default 100000000)

    --log-file-num-backups           number of log files to keep (default 10)

    --log-file-prefix=PATH           Path prefix for log files. Note that if you
                                    are running multiple tornado processes,
                                    log_file_prefix must be different for each
                                    of them (e.g. include the port number)

    --log-rotate-interval            The interval value of timed rotating
                                    (default 1)

    --log-rotate-mode                The mode of rotating files(time or size)
                                    (default size)

    --log-rotate-when                specify the type of TimedRotatingFileHandler
                                    interval other options:('S', 'M', 'H', 'D',
                                    'W0'-'W6') (default midnight)

    --log-to-stderr                  Send log output to stderr (colorized if
                                    possible). By default use stderr if
                                    --log_file_prefix is not set and no other
                                    logging is configured.

    --logging=debug|info|warning|error|none 
                                    Set the Python log level. If 'none', tornado
                                    won't touch the logging configuration.
                                    (default info)

.. code:: bash

    # start a http server with specified listen address and listen port
    wssh --address='2.2.2.2' --port=8000

    # start a https server, certfile and keyfile must be passed
    wssh --certfile='/path/to/cert.crt' --keyfile='/path/to/cert.key'

    # missing host key policy
    wssh --policy=reject

    # logging level
    wssh --logging=debug

    # log to file
    wssh --log-file-prefix=main.log

    # more options
    wssh --help

Browser console
~~~~~~~~~~~~~~~

.. code:: javascript

    // connect to your ssh server
    wssh.connect(hostname, port, username, password, privatekey, passphrase, totp);

    // pass an object to wssh.connect
    var opts = {
      hostname: 'hostname',
      port: 'port',
      username: 'username',
      password: 'password',
      privatekey: 'the private key text',
      passphrase: 'passphrase',
      totp: 'totp'
    };
    wssh.connect(opts);

    // without an argument, wssh will use the form data to connect
    wssh.connect();

    // set a new encoding for client to use
    wssh.set_encoding(encoding);

    // reset encoding to use the default one
    wssh.reset_encoding();

    // send a command to the server
    wssh.send('ls -l');

Custom Font
~~~~~~~~~~~

To use custom font, put your font file in the directory
``webssh/static/css/fonts/`` and restart the server.

URL Arguments
~~~~~~~~~~~~~

Support passing arguments by url (query or fragment) like following
examples:

Passing form data (password must be encoded in base64, privatekey not
supported)

.. code:: bash

    http://localhost:8888/?hostname=xx&username=yy&password=str_base64_encoded

Passing a terminal background color

.. code:: bash

    http://localhost:8888/#bgcolor=green

Passing a user defined title

.. code:: bash

    http://localhost:8888/?title=my-ssh-server

Passing an encoding

.. code:: bash

    http://localhost:8888/#encoding=gbk

Passing a command executed right after login

.. code:: bash

    http://localhost:8888/?command=pwd

Passing a terminal type

.. code:: bash

    http://localhost:8888/?term=xterm-256color

Use Docker
~~~~~~~~~~

Start up the app

::

    docker-compose up

Tear down the app

::

    docker-compose down

Tests
~~~~~

Requirements

::

    pip install pytest pytest-cov codecov flake8 mock

Use unittest to run all tests

::

    python -m unittest discover tests

Use pytest to run all tests

::

    python -m pytest tests

Deployment
~~~~~~~~~~

Running behind an Nginx server

.. code:: bash

    wssh --address='127.0.0.1' --port=8888 --policy=reject

.. code:: nginx

    # Nginx config example
    location / {
        proxy_pass http://127.0.0.1:8888;
        proxy_http_version 1.1;
        proxy_read_timeout 300;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $http_host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Real-PORT $remote_port;
    }

Running as a standalone server

.. code:: bash

    wssh --port=8080 --sslport=4433 --certfile='cert.crt' --keyfile='cert.key' --xheaders=False --policy=reject

Tips
~~~~

-  For whatever deployment choice you choose, don't forget to enable
   SSL.
-  By default plain http requests from a public network will be either
   redirected or blocked and being redirected takes precedence over
   being blocked.
-  Try to use reject policy as the missing host key policy along with
   your verified known\_hosts, this will prevent man-in-the-middle
   attacks. The idea is that it checks the system host keys
   file("~/.ssh/known\_hosts") and the application host keys
   file("./known\_hosts") in order, if the ssh server's hostname is not
   found or the key is not matched, the connection will be aborted.

.. |PyPI - Python Version| image:: https://img.shields.io/pypi/pyversions/webssh.svg
.. |PyPI| image:: https://img.shields.io/pypi/v/webssh.svg
.. |Login| image:: https://github.com/swjpilot/webssh/raw/master/preview/login.png
.. |Terminal| image:: https://github.com/swjpilot/webssh/raw/master/preview/terminal.png

