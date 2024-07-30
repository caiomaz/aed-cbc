# Ferramenta de Criptografia e Descriptografia CBC

Este repositório contém uma implementação de criptografia e descriptografia usando o modo CBC (Cipher Block Chaining) com operações XOR. Este sistema permite cifrar e decifrar textos usando uma chave e um vetor de inicialização (IV) fornecidos pelo usuário ou valores padrão.
Estrutura do Projeto

- **.gitignore**: Arquivo para especificar quais arquivos ou diretórios o Git deve ignorar.
- **main.py**: Contém a implementação das funções de criptografia e descriptografia, além de uma interface de linha de comando para interação com o usuário.
- **README.md**: Este arquivo, contendo informações sobre o projeto, incluindo uma visão geral da estrutura de diretórios, descrição dos arquivos e uma explicação detalhada do código contido em main.py.

## Executar o Código

Execute o seguinte comando para executar o script de criptografia e descriptografia:

```
python main.py
```

## Detalhes da Implementação em main.py
### Funções Principais

- `xor_bytes(a, b)`: Realiza a operação XOR entre dois blocos de bytes.
- `cifrar_cbc(texto, chave, iv)`: Cifra o texto usando o modo CBC.
- `descriptografar_cbc(texto_cifrado, chave, iv)`: Descriptografa o texto cifrado usando o modo CBC.

## Funções de Criptografia e Descriptografia

`Função xor_bytes(a, b)`: Realiza a operação XOR byte a byte entre dois blocos de bytes a e b.

`Função cifrar_cbc(texto, chave, iv)`: Cifra o texto em blocos, aplicando XOR com o bloco anterior ou IV e cifrando com a chave.

`Função descriptografar_cbc(texto_cifrado, chave, iv)`:
Descriptografa o texto cifrado, aplicando XOR com o bloco anterior ou IV e removendo o padding.


## Exemplo de Uso

```
python main.py

Escolha a operação desejada:
1. Criptografar texto
2. Descriptografar texto
3. Sair
Operação: 1
Digite o texto a ser criptografado: Hello, World!
Escolha o formato de saída:
1. Hexadecimal
2. Base64
3. Binário
Formato: 1
Deseja inserir a chave e o vetor de inicialização (IV)? (s/n): n
Texto cifrado: <resultado em hexadecimal>
```