from typing import List

def avalia(polinomio: List[float], x: float) -> float:
    grau = len(polinomio) - 1
    res = 0
    for i in range(len(polinomio)):
        res += polinomio[i] * (x ** (grau - i))
    
    return res

def fpm(polinomio: List[float], a: float, b: float, tol: float, maxIter: int=5) -> float:
    fa = avalia(polinomio, a)
    fb = avalia(polinomio, b)
    
    i = 0
    while i < maxIter:
        x = (a*fb -b*fa) / (fb - fa)
        if x - a < tol:
            print(f'tentativas: {i}')
            return x
        
        i += 1
        fx = avalia(polinomio, x)
        if fa * fx < 0:
            b = x
        if fa * fx > 0:
            a = x

    print('FALHA!!!')


def main():
    polinomio = [2, 3, -1]
    raiz = fpm(polinomio, 0, 1, 0.00005, maxIter=30)
    print(f'raiz = {raiz}')
    print(f'polinomio aplicado na raiz encontrada: {avalia(polinomio, raiz)}')


if __name__ == '__main__':
    main()
