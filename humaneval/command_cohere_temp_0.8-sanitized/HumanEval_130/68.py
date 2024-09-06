def tri(n):
    out = []
    x, y, z = 1, 3, 2
    while len(out) < n + 1:
        if len(out) % 2 == 0:
            out.append(x)
            x = x + y + z
            y = z
        else:
            out.append(z)
            z = x + y + z
            x = y
        y = x
    return out