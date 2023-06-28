import socket

def cliente():
    # Cria um socket TCP/IP
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Define o endereço IP e porta do servidor
    endereco_servidor = ('localhost', 5000)
    
    try:
        # Estabelece uma conexão com o servidor
        cliente_socket.connect(endereco_servidor)
        
        while True:
            # Solicita ao usuário que digite uma mensagem
            mensagem = input("Digite uma mensagem (ou 'exit' para sair): ")
            
            if mensagem == 'exit':
                break
            
            # Envia a mensagem para o servidor
            cliente_socket.send(mensagem.encode())
        
    finally:
        # Fecha a conexão com o servidor
        cliente_socket.close()

cliente()
