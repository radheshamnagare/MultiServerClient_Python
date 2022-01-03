# MultiServerClient_Python

compile/run command for 'server.py':
  python3 server.py <PORT>

compile/run command for 'client.py':
 python3 client.py <IP> <PORT>
 
 like bellow we can rum many of instances with differnt port
       python3 server.py 5001
       python3 lient.py 127.0.0.1 5001
          
 Implemtation part :
    
    we want to run many server/machine and also handle many of client/program and each of server machine  
    will handle at least 10 client 
    
    so how i approched this problem :
    
     i'm not used any common buffer in server/machine and file should be arbitary large or small and some part
     of file my present in other machine .the reasone is if we used common buffer then problem may happen data 
     inconsistant and we will get wrong data.also aim is handle many of client . that's chunk of byte of file i 
     send sequencialy to respective client .the advantage to sending chunk of byte is we used minimum memory so 
     that we can handle many of client/program concurently. 
     python allow you to load a data of file once that may happen memory overflow or other client/program can't 
     get a chance to comminucate server/machine .
     also the file should not a specific type and i tried differnt types of files .for part of file you shall 
     see 'file_diverder' directory and part file save in differnt machine with same file name .
     some of signal also handle like ctr+c so can terminate safly. 
     
     Port : 5000-6000 i used
     Directory structure :
      
      For server the datasource directory naming follow like as d5000,d5001,d5003
      For client/program one local directory we follow as 'localStorage'
     
      Note : we don't need to create directory manualy program will handle automaticaly for both server/machine
      and client/program
      
      and client/program
      
      
