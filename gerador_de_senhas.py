import secrets
import string

# define the alfabeto
letras = string.ascii_letters
digitos = string.digits
caracteres_especiais = string.punctuation

alfabeto = letras + digitos + caracteres_especiais

# fix password length
tamanho_da_senha = 40

# generate a password string
senha = ''
for i in range(tamanho_da_senha):
  senha += ''.join(secrets.choice(alfabeto))

print(senha)

# generate password meeting constraints
while True:
  senha = ''
  for i in range(tamanho_da_senha):
    senha += ''.join(secrets.choice(alfabeto))

  if (any(char in caracteres_especiais for char in senha) and
      sum(char in digitos for char in senha)>=2):
          break
print(senha)