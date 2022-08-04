# Traffic Light Secure Headers - TLSecHead


🚦 **Traffic Light Secure Headers**  is a tool that aims to retrieve the response headers from a website (URL), or from a file containing a list of URLs, and compare it with a list of security response headers. As a result we have:

- $\textcolor{red}{Deprecated\ Headers}$
- $\textcolor{yellow}{Missing\ Headers}$
- $\textcolor{green}{Found\ Headers}$

This tool was completely based on the [OWASP Secure Headers Project](https://owasp.org/www-project-secure-headers/).

But for the purpose of making the tool easier, I considered Working Draft Headers as Active Headers and Almost Deprecated Headers as Deprecated Headers. For more information, access the OWASP project. 👏

## How to use

Its use is very simple,

Viewing the menu,

```
# python3 TLSecHead.py -h

or

# python3 TLSecHead.py --help

______ ________________________________ ______
  _____ _    ___         _  _             _ 
 |_   _| |  / __| ___ __| || |___ __ _ __| |
   | | | |__\__ \/ -_) _| __ / -_) _` / _` |
   |_| |____|___/\___\__|_||_\___\__,_\__,_|

______ _______ By @hihackthis _________ ______

                    [X]                    
                    [>]                    
                    [#]                     

usage: TLSecHead.py [-h] [-u URL | -f FILE] [-ua AGENT]

------ Traffic Light Secure Headers ------

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     enter URL [http:// | https://]
  -f FILE, --file FILE  enter the file with URLs
```

Only two options,

1. A single entire URL (don't forget http:// or https://)

```
python3 TLSecHead.py -u https://www.example.com

or

python3 TLSecHead.py --url https://www.example.com
```

2. A file containing a list of multiple URLs, one under the other.

```
$ cat list_url.txt 
https://www.example1.com
https://www.example2.com
http://www.example3.com
https://www.example4.com
```

Just enter the absolute or relative path of the file:

```
python3 TLSecHead.py -f path/list_url.txt

or

python3 TLSecHead.py --file path/list_url.txt
```


Note that the file is text only:

```
$ file list_url.txt 
list_url.txt: ASCII text
```

## Install 

```
git clone https://github.com/hihackthis/TLSecHead
cd TLSecHead
pip3 install -r requirements.txt

Done :-)
```

## Good to know

The tool uses a list of User-Agents randomly to query the headers of websites. Feel free to edit it with your preferred User-Agents.
