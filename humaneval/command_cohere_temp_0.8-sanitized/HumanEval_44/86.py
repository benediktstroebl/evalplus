def change_base(x, base):
    return str(x).encode([(str(i), str(base)) for i in range(1, base + 1) if x >= i][x]).decode('utf-8')