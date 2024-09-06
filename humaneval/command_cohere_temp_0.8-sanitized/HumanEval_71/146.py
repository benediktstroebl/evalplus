def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a - b) > 1e-6 or abs(s - a - c) > 1e-6 or abs(s - b - c) > 1e-6:
        return -1
    else:
        area = (a * b * (c ** 2) + b * c * (a ** 2) + c * a * (b ** 2)) ** 0.5
        return round(area, 2)