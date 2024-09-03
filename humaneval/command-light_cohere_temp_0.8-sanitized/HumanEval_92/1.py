def any_int(x, y, z):
    return (x == y + z) and (type(x) == int and type(y) == int and type(z) == int)
x = any_int(5, 2, 7)
y = any_int(3, 2, 2)
z = any_int(3, -2, 1)