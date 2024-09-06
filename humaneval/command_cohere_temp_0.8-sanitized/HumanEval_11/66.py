def string_xor(a, b):
    return fern(a + b)
def fern(p):
    return f'{p[:1]}{p[1:]^p[0:-1]}{p[-1]}'