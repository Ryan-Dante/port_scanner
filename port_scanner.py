import socket

def get_open_ports(target, port_range, verbose = False):
    ip = ""
    open_ports = []
    try:
        ip = socket.gethostbyname(target)
        for port in range(port_range[0], port_range[1] + 1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.1)
            result = s.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            s.close()
    
    except socket.gaierror:
        return "Error: Invalid hostname"
    except socket.error:
        return "Error: Invalid port range"
    except ip == "":
        return "Error: Invalid IP address"
    
    if verbose:
        output = f"Open ports for {target} ({ip})\nPORT     SERVICE\n"
        for port in open_ports:
            try:
                service = socket.getservbyport(port)
            except:
                service = ""
            output += f"{port:<9}{service}\n"
        return(output)
    else:
        return(open_ports)