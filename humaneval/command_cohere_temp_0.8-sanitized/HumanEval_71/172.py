def triangle_area(a, b, c):
    s = sum([a, b, c])
    if len(set(x + y for x, y in zip(a, b, c)))>1 and max(a, b, c) <= s / 2:
        return round(0.5 * (s * (s-a) * (s-b) * (s-c))**0.5, 2)
    else:
        return -1