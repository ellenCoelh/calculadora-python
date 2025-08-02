def soma(a, b):
    """
    Realiza a soma de dois números.
    
    Parâmetros:
    a (int/float): Primeiro número
    b (int/float): Segundo número
    
    Retorna:
    int/float: Resultado da soma
    """
    return a + b

def restoDivisao(a, b):
    '''
    Realiza a operação de resto de divisao entre dois numeros.
    parâmetros:
    a(int/float):primeiro número
    b(int/float):segundo numero
    retorna:
    int/float: Resultado da soma
    '''
    return a % b
    

if __name__ == "__main__":
    print("Teste da função soma:")
    print(f"2 + 3 = {soma(2, 3)}") 
    print(f"5.5 + 4.5 = {soma(5.5, 4.5)}") 
    print(f'2 + 2 = {soma(2, 2)}')
    print('que galerinha massa, façam essa conta:')
    print(f'100 + 100 = {soma(100, 100)}')
    print(f' 3 + 10 = {soma(3,10)}') 
    print("vamo genteee (menos ana e seu tema branco)")
    print(f"resto divisão {restoDivisao(5,2)}")