def any_int(x, y, z):
    return all([x + y == z and isinstance(x, int) and isinstance(y, int)] for x, y, z in [x, y, z])