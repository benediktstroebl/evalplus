def triangle_area(a, b, c):
    s = lambda x, y: x + y - c
    return round(0.5 * np.sqrt(max(s(a, b), s(b, c), s(c, a))), 2) if max(s(a, b), s(b, c), s(c, a)) else -1