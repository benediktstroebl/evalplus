def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - max(s)) < 1e-5:
        area = (max(a, b, c) * (s - max(a, b, c)) / 2)
        return round(area, 2)
    else:
        return -1