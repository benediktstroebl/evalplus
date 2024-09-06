def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - max(s)) < 1e-5:
        area = (a * b * math.sqrt(3) / 2)
        return round(area, 2)
    else:
        return -1