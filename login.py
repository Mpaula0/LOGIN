import PySimpleGUI as sg


def main():
    sg.theme('Black2')

    layout = [
        [sg.Text('Cadastro', font=('Helvetica', 20))],
        [sg.Text('Nome de usuário:'), sg.InputText(key='-username-')],
        [sg.Text('Senha:'), sg.InputText(key='-password-', password_char='*')],
        [sg.Button('Entrar'), sg.Button('Esqueceu a senha')],
    ]

    window = sg.Window('Tela de Login', layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == 'Entrar':
            username = values['-username-']
            password = values['-password-']

            if username == 'Miguel' and password == 'abc':
                sg.popup('Bem-vindo!')
            else:
                sg.popup_error('Login inválido. Por favor, tente novamente.')

        elif event == 'Esqueceu a senha':
            email = sg.popup_get_text('Digite seu e-mail:')

            sg.popup('Perfeito! Solicitação de troca de senha enviada.')

    window.close()


if _name_ == '_main_':
    main()