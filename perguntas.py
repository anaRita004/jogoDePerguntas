perguntas_respostas = {
    "Qual é a capital do Brasil?": "Brasília",
    "Quantos planetas existem no sistema solar?": "Oito",
    "Quem escreveu 'Dom Quixote'?": "Miguel de Cervantes",
    "Qual é o maior animal terrestre?": "Elefante africano",
    "Quem pintou a Mona Lisa?": "Leonardo da Vinci"
}

def formatar_resposta(resposta):
    return resposta.strip().lower()

print("Bem-vindo ao jogo de Trívia!")

pontuacao = 0
for pergunta, resposta_correta in perguntas_respostas.items():
    print("\nPergunta:", pergunta)
    resposta_usuario = input("Sua resposta: ").strip()
    
    if formatar_resposta(resposta_usuario) == formatar_resposta(resposta_correta):
        print("Resposta correta! 🎉")
        pontuacao += 1
    else:
        print(f"Resposta incorreta. 😔 A resposta correta é: {resposta_correta}")

print("\nFim do jogo!")
print(f"Sua pontuação final é: {pontuacao} pontos.")
