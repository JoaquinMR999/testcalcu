def sumar (a, b):
    return a + b

def resta (a, b):
    return a - b

def multi (a, b):
    return a * b

def divide (a, b):
    if b == 0:
        raise ValueError("No puede dividir entre 0")
    return a / b

if __name__ == '__main__':
    print (sumar(5,3))
    print (resta(5,3))
    print (multi(5,3))
    print (divide(5,3))