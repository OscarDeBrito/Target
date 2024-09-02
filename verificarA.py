def conta_As(texto: str) -> None:
    texto_minusculo = texto.lower() 
    quantidade = texto_minusculo.count('a')  

    if quantidade > 0:
        print(f" quantidades de 'a' na frase: {quantidade} .")
    else:
        print("a letra 'a' não aparece na string.")

texto = input("Digite uma string: ")
conta_As(texto)
