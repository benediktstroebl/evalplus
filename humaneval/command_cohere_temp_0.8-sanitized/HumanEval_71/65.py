def triangle_area(a, b, c):
    s = sum(a, b, c)
    if abs(s - a) > 1e-9 and abs(s - b) > 1e-9 and abs(s - c) > 1e-9:
        area = (a * b * (c * (c - a - b) / (2 * s))).round(2)
    else:
        area = -1
    return area