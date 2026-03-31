import random
from collections import defaultdict

class BigramModel:
    def __init__(self):
        self.modelo = defaultdict(list)

    def treinar(self, texto):
        palavras = texto.lower().split()

        for i in range(len(palavras) - 1):
            palavra_atual = palavras[i]
            proxima_palavra = palavras[i + 1]

            self.modelo[palavra_atual].append(proxima_palavra)

    def gerar_texto(self, palavra_inicial, tamanho=10):
        if palavra_inicial not in self.modelo:
            return "Palavra inicial não encontrada no corpus."

        palavra_atual = palavra_inicial
        resultado = [palavra_atual]

        for _ in range(tamanho - 1):
            proximas = self.modelo.get(palavra_atual)

            if not proximas:
                break

            palavra_atual = random.choice(proximas)
            resultado.append(palavra_atual)

        return " ".join(resultado)


def carregar_corpus(caminho):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        return arquivo.read()


if __name__ == "__main__":
    modelo = BigramModel()

    texto = carregar_corpus("exemplo_corpus.txt")
    modelo.treinar(texto)

    palavra = input("Digite uma palavra inicial: ")
    frase = modelo.gerar_texto(palavra, tamanho=15)

    print("Texto gerado:")
    print(frase)
