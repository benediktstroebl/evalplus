def any_int(x, y, z):
    return x == y + z and all(type(i) == int for i in (x, y, z))