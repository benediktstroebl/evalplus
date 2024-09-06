def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - max(s)) < 1e-5:
        area = (a * b * (c ** 2) + b * c * (a ** 2) + c * a * (b ** 2)) ** 0.5
        return round(area, 2)
    else:
        return -1