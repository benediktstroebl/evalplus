def triangle_area(a, b, c):
    s = sum(i for i in [a, b, c] if i != max(a, b, c))
    if s == 0:
        return round(0.5 * (a * b), 2)
    elif s == 2:
        return round(0.5 * (a * c), 2)
    elif s == 3:
        return round(0.5 * (b * c), 2)
    else:
        return -1