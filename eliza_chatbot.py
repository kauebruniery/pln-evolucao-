import re
import random

class ElizaChatbot:
    def __init__(self):
        # Padrões simples usando regex
        self.padroes = [
            (r"me sinto (.*)", [
                "Por que você se sente {0}?",
                "Desde quando você se sente {0}?",
                "O que faz você se sentir {0}?"
            ]),

            (r"eu sou (.*)", [
                "Como você se tornou {0}?",
                "Você gosta de ser {0}?",
                "Por que você diz que é {0}?"
            ]),

            (r"preciso de (.*)", [
                "Por que você precisa de {0}?",
                "O que aconteceria se você tivesse {0}?"
            ]),

            (r"oi|olá|ola", [
                "Olá! Como você está hoje?",
                "Oi! Sobre o que você gostaria de conversar?"
            ]),

            (r"(.*)", [
                "Conte-me mais sobre isso.",
                "Interessante... continue.",
                "Como isso faz você se sentir?"
            ])
        ]

    def responder(self, texto_usuario):
        texto_usuario = texto_usuario.lower()

        for padrao, respostas in self.padroes:
            match = re.match(padrao, texto_usuario)

            if match:
                resposta = random.choice(respostas)

                if "{0}" in resposta and match.groups():
                    return resposta.format(match.group(1))
                else:
                    return resposta

    def iniciar_conversa(self):
        print("ELIZA: Olá, eu sou sua terapeuta virtual. Digite 'sair' para encerrar.")

        while True:
            entrada = input("Você: ")

            if entrada.lower() == "sair":
                print("ELIZA: Foi bom conversar com você.")
                break

            resposta = self.responder(entrada)
            print("ELIZA:", resposta)


if __name__ == "__main__":
    chatbot = ElizaChatbot()
    chatbot.iniciar_conversa()
