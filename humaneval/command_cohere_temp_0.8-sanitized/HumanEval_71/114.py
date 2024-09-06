def triangle_area(a, b, c):
    s = sum(i for i in [a, b, c] if i != max(a, b, c))
    if len(s) == 2 and max(a, b, c) - min(a, b, c) > 0.0:
        r = (max(a, b, c) * (s[0] + s[1]) / 2) / (max(a, b, c) - min(a, b, c))
        return round(r, 2)
    else:
        return -1