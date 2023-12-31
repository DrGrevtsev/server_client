
import socket   


## func for the connection of the host and the port you open on 

def host_connection():
    host = '127.0.0.1'
    port = 1338
    
    return host, port

#Creat a listening on the port
def listening(host,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))
    s.listen(1)
    print(f'Server is listen on port: {port} and wait for connection ')
    
    return s

 
#the creation of the connection with  the remote ip
def server_connection(s):
    sock_conn, remote_addr = s.accept()
    remote_ip, remote_port = remote_addr
    print(f'You are connected to remote host: {remote_ip}, on  remote port: {remote_port} ')
    sock_conn.send(b'Server says: Hello welcome\n')
    
    while sock_conn:
        status = data_recive(sock_conn)
        if status == 'exit':
           return 'exit'
        stats = send_data(sock_conn)
        if stats == 'exit':
           return 'exit'
        
      
def data_recive(sock_conn):
    in_data = sock_conn.recv(1024)
    in_data = in_data.decode('utf-8')
    if not in_data:
        return 'exit'
    elif 'exit' in in_data:
        return 'exit'
   
    elif in_data != None:
        print(f'Client: {in_data}')
        return ""
    
    
        
    
def send_data(sock_conn):
    out_d = input('Server: ')
    if out_d == 'exit':
        sock_conn.send(out_d.encode())
        return 'exit'
    else:
        sock_conn.send(out_d.encode())
    
          
   
def break_connection(s):
    s.close()
              




        
    
def main():
    
    host, port = host_connection()
    server_conn = listening(host,port)
    server_status = server_connection(server_conn)
    if 'exit' in server_status:
        break_connection(server_conn)
        print('\nConnection have ended\n  ')
    

        
try:
    main()

except KeyboardInterrupt:
    print('\nThank you and Good bye ')