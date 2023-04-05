import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class JogoTabuada(QWidget):
    def __init__(self):
        super().__init__()
        self.acertos = 0
        self.erros = 0
        self.inicializar_ui()

    def inicializar_ui(self):
        self.setWindowTitle('Jogo da Tabuada')
        self.layout = QVBoxLayout()

        # Cria e exibe a pergunta de multiplicação
        self.pergunta = QLabel()
        self.gerar_pergunta()
        self.layout.addWidget(self.pergunta)

        # Campo para inserir a resposta
        self.entrada_resposta = QLineEdit()
        self.layout.addWidget(self.entrada_resposta)

        # Botão para verificar a resposta
        self.botao_verificar = QPushButton('Verificar Resposta')
        self.botao_verificar.clicked.connect(self.verificar_resposta)
        self.layout.addWidget(self.botao_verificar)

        # Labels para exibir a quantidade de acertos e erros
        self.label_acertos = QLabel(f'Acertos: {self.acertos}')
        self.layout.addWidget(self.label_acertos)
        self.label_acertos.setStyleSheet("color: blue")

        self.label_erros = QLabel(f'Erros: {self.erros}')
        self.layout.addWidget(self.label_erros)
        self.label_erros.setStyleSheet("color: red")

        self.setLayout(self.layout)
        self.setFixedSize(300, 150)

    # Gera uma pergunta de multiplicação aleatória
    def gerar_pergunta(self):        
        self.numero1 = random.randint(1, 10)
        self.numero2 = random.randint(1, 10)
        self.pergunta.setText(f'Qual é o resultado de {self.numero1} x {self.numero2}?')

    # Verifica se a resposta inserida está correta ou incorreta
    def verificar_resposta(self):        
        try:
            resposta = int(self.entrada_resposta.text())
        except ValueError:
            QMessageBox.warning(self, 'Entrada inválida', 'Digite um número inteiro válido.')
            return

        if resposta == self.numero1 * self.numero2:
            QMessageBox.information(self, 'Correto!', 'Parabéns! Sua resposta está correta.')
            self.acertos += 1
        else:
            QMessageBox.critical(self, 'Incorreto', 'A resposta está incorreta. Tente novamente.')
            self.erros += 1

        # Atualiza os rótulos de acertos e erros
        self.label_acertos.setText(f'Acertos: {self.acertos}')
        self.label_erros.setText(f'Erros: {self.erros}')
        self.entrada_resposta.clear()
        self.gerar_pergunta()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    jogo = JogoTabuada()
    jogo.show()
    sys.exit(app.exec_())
