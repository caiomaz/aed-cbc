import base64

def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

def cifrar_cbc(texto, chave, iv):
    tamanho_bloco = len(chave)
    texto_cifrado = b''

    # Pad o texto para que seu comprimento seja múltiplo do tamanho do bloco
    padding_length = tamanho_bloco - (len(texto) % tamanho_bloco)
    texto += bytes([padding_length] * padding_length)

    # Divide o texto em blocos de tamanho igual ao da chave
    blocos = [texto[i:i+tamanho_bloco] for i in range(0, len(texto), tamanho_bloco)]

    bloco_anterior = iv

    for bloco in blocos:
        # Aplica XOR com o bloco anterior (ou IV para o primeiro bloco)
        bloco = xor_bytes(bloco, bloco_anterior)
        # Cifra o bloco (neste exemplo, usamos XOR com a chave)
        bloco_cifrado = xor_bytes(bloco, chave)
        texto_cifrado += bloco_cifrado
        # Atualiza o bloco anterior
        bloco_anterior = bloco_cifrado

    return texto_cifrado

def descriptografar_cbc(texto_cifrado, chave, iv):
    tamanho_bloco = len(chave)
    texto_descriptografado = b''

    # Divide o texto cifrado em blocos de tamanho igual ao da chave
    blocos = [texto_cifrado[i:i+tamanho_bloco] for i in range(0, len(texto_cifrado), tamanho_bloco)]

    bloco_anterior = iv

    for bloco in blocos:
        # Descriptografa o bloco (neste exemplo, usamos XOR com a chave)
        bloco_descriptografado = xor_bytes(bloco, chave)
        # Aplica XOR com o bloco anterior (ou IV para o primeiro bloco)
        bloco_descriptografado = xor_bytes(bloco_descriptografado, bloco_anterior)
        texto_descriptografado += bloco_descriptografado
        # Atualiza o bloco anterior
        bloco_anterior = bloco

    # Remove padding
    padding_length = texto_descriptografado[-1]
    texto_descriptografado = texto_descriptografado[:-padding_length]

    return texto_descriptografado

def main():
    while True:
        print("\nEscolha a operação desejada:")
        print("1. Criptografar texto")
        print("2. Descriptografar texto")
        print("3. Sair")

        operacao = input("Digite o número correspondente à operação desejada: ")

        if operacao == '1':
            texto = input("Digite o texto a ser criptografado: ").encode('utf-8')

            usar_padrao = input("Deseja inserir a chave e o vetor de inicialização (IV)? (s/n): ")

            if usar_padrao.lower() == 's':
                chave = input("Digite a chave (em texto, 16 bytes): ").encode('utf-8')
                iv = input("Digite o vetor de inicialização (IV) (em texto, 16 bytes): ").encode('utf-8')

                if len(chave) != 16 or len(iv) != 16:
                    print("A chave e o IV devem ter 16 bytes.")
                    continue
            else:
                chave = b'0123456789abcdef'  # Chave padrão de 16 bytes
                iv = b'abcdef9876543210'     # IV padrão de 16 bytes
                print(f"Usando chave padrão: {chave.decode('utf-8')}")
                print(f"Usando vetor de inicialização (IV) padrão: {iv.decode('utf-8')}")

            texto_cifrado = cifrar_cbc(texto, chave, iv)
            print("\nEscolha o formato de saída:")
            print("1. Hexadecimal")
            print("2. Base64")
            print("3. Binário")

            formato_saida = input("Digite o número correspondente ao formato desejado: ")

            if formato_saida == '1':
                print("Texto cifrado em hexadecimal:", texto_cifrado.hex())
            elif formato_saida == '2':
                print("Texto cifrado em base64:", base64.b64encode(texto_cifrado).decode('utf-8'))
            elif formato_saida == '3':
                print("Texto cifrado em binário:", ''.join(format(byte, '08b') for byte in texto_cifrado))
            else:
                print("Formato inválido")
        
        elif operacao == '2':
            print("\nEscolha o formato do texto cifrado:")
            print("1. Hexadecimal")
            print("2. Base64")
            print("3. Binário")

            escolha = input("Digite o número correspondente ao formato desejado: ")

            if escolha == '1':
                hex_texto_cifrado = input("Digite o texto cifrado em formato hexadecimal: ")
                texto_cifrado = bytes.fromhex(hex_texto_cifrado)
            elif escolha == '2':
                base64_texto_cifrado = input("Digite o texto cifrado em formato base64: ")
                texto_cifrado = base64.b64decode(base64_texto_cifrado)
            elif escolha == '3':
                bin_texto_cifrado = input("Digite o texto cifrado em formato binário: ")
                texto_cifrado = int(bin_texto_cifrado, 2).to_bytes((len(bin_texto_cifrado) + 7) // 8, byteorder='big')
            else:
                print("Formato inválido")
                continue

            usar_padrao = input("Deseja inserir a chave e o vetor de inicialização (IV)? (s/n): ")

            if usar_padrao.lower() == 's':
                chave = input("Digite a chave (em texto, 16 bytes): ").encode('utf-8')
                iv = input("Digite o vetor de inicialização (IV) (em texto, 16 bytes): ").encode('utf-8')

                if len(chave) != 16 or len(iv) != 16:
                    print("A chave e o IV devem ter 16 bytes.")
                    continue
            else:
                chave = b'0123456789abcdef'  # Chave padrão de 16 bytes
                iv = b'abcdef9876543210'     # IV padrão de 16 bytes
                print(f"Usando chave padrão: {chave.decode('utf-8')}")
                print(f"Usando vetor de inicialização (IV) padrão: {iv.decode('utf-8')}")

            texto_descriptografado = descriptografar_cbc(texto_cifrado, chave, iv)

            try:
                texto_descriptografado_utf8 = texto_descriptografado.decode('utf-8')
                print("Texto descriptografado:", texto_descriptografado_utf8)
            except UnicodeDecodeError:
                print("Erro na decodificação do texto descriptografado. Conteúdo bruto:", texto_descriptografado)

        elif operacao == '3':
            break
        else:
            print("Operação inválida. Tente novamente.")

if __name__ == "__main__":
    main()
