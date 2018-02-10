from sympy import *

x = Symbol('x', commutative=False)
y = Symbol('y', commutative=False)
X = Symbol('X', commutative=False)
Y = Symbol('Y', commutative=False)
eps = Symbol('\epsilon')

def magnus(w, n):
    """
    The 'Magnus' map
    """
    expr = w.subs(x,1+eps*X).subs(y,1+eps*Y) - 1
    return limit(expr / eps**n, eps, 0)

def degree(w):
    if w == 1:
        return 10000 # should be inf actually
    d = 1
    while magnus(w,d) == 0:
        d += 1
    return d

def decode_word(n):
    """
    basic map ints -> words starting with letter x
    """
    letters = [x, y, x**-1, y**-1]
    w = x
    i = 0 # index of letter
    length = 1
    while n > 0:
        i = (i + n % 3 - 1) % 4 # change by 1, 0, or -1
        w *= letters[i]
        n //= 3
        length += 1
    return w, length

if __name__ == '__main__':
    import sys
    try:
        N = int(sys.argv[1])
    except:
        N = 10000
        print('No N provided, so I\'m putting N={}.'.format(N))
    alpha = {}
    for n in range(N):
        w, l = decode_word(n)
        d = degree(w)
        if d not in alpha:
            alpha[d] = l
            print(d, l, w)