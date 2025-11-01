# chatbot_agendamento.py
from datetime import datetime

def menu_principal():
    print("👋 Olá! Bem-vindo ao Agendamento Fácil!")
    print("1 - Fazer um agendamento")
    print("2 - Como funciona o pagamento?")
    print("3 - Dúvidas")
    print("4 - Falar com um atendente")

def fazer_agendamento():
    nome = input("Qual o seu nome? ")
    servico = input("Qual serviço você deseja? ")
    dia = input("Qual dia você prefere (dd/mm/aaaa)? ")
    hora = input("Qual horário? ")

    print(f"\nResumo do agendamento:")
    print(f"Cliente: {nome}")
    print(f"Serviço: {servico}")
    print(f"Data: {dia} às {hora}")
    pagar = input("Deseja pagar agora? (Pix/Cartão/Nao) ")

    print("\nEnviando informações para confirmação da empresa... ✅")

def iniciar():
    menu_principal()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        fazer_agendamento()
    elif opcao == "2":
        print("Você pode pagar via Pix ou Cartão.")
    elif opcao == "3":
        print("Dúvidas frequentes: horários, valores, cancelamentos...")
    elif opcao == "4":
        print("Transferindo para atendente humano...")
    else:
        print("Opção inválida.")

# Iniciar chatbot
iniciar()
# chatbot.py
from datetime import datetime

def menu_principal():
    print("\n👋 Bem-vindo ao *Agendamento Fácil*!")
    print("Escolha uma opção:")
    print("1️⃣ Fazer um agendamento")
    print("2️⃣ Como funciona o pagamento?")
    print("3️⃣ Dúvidas")
    print("4️⃣ Falar com um atendente")

def fazer_agendamento():
    nome = input("➡️ Qual o seu nome? ")
    servico = input("➡️ Qual serviço você deseja? ")
    dia = input("➡️ Qual dia (dd/mm/aaaa)? ")
    hora = input("➡️ Qual horário? ")

    print("\n📅 Resumo do agendamento:")
    print(f"👤 Cliente: {nome}")
    print(f"💈 Serviço: {servico}")
    print(f"🗓️ Data: {dia} às {hora}")

    pagamento = input("\nDeseja pagar agora (Pix/Cartão/Nao)? ").strip().lower()
    if pagamento in ["pix", "cartão", "cartao"]:
        print("🔗 Enviando link/chave de pagamento...")
    else:
        print("💬 Pagamento será feito no local.")

    print("\n✅ Enviando informações para confirmação da empresa...")
    print("📨 Agendamento pendente de confirmação.\n")

def chatbot():
    while True:
        menu_principal()
        opcao = input("Digite o número da opção: ")

        if opcao == "1":
            fazer_agendamento()
        elif opcao == "2":
            print("\n💳 Pagamento pode ser feito via Pix ou Cartão (link seguro).")
        elif opcao == "3":
            print("\n❓ Dúvidas frequentes: horários, valores, cancelamentos...")
        elif opcao == "4":
            print("\n👩‍💼 Transferindo para atendente humano...")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    chatbot()
