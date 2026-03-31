from transformers import pipeline


def executar_modelo():
    print("Carregando modelo GPT-2...")

    gerador = pipeline(
        "text-generation",
        model="gpt2"
    )

    prompt = input("Digite um início de frase: ")

    resultado = gerador(
        prompt,
        max_length=50,
        num_return_sequences=1
    )

    print("\nTexto gerado:")
    print(resultado[0]["generated_text"])


if __name__ == "__main__":
    executar_modelo()
