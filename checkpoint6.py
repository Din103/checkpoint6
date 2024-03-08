class Usuario:
    def __init__(self, usuario, contraseña):
        self.usuario = usuario
        self.contraseña = contraseña
usuario = Usuario("Pedro", "123456789")
print("Usuario:", usuario.usuario)
print("Contraseña:", usuario.contraseña)