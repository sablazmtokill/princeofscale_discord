import random

symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"

def password_func():
    psswrd = []
    for i in range(20):
        psswrd.append(symbols[random.randint(0, 73)])
    return ''.join(psswrd)

