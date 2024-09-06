def triangle_area(a, b, c):
    s = sum(a, b, c)
    if s == a + b or s == b + c or s == a + c:
        area = (a * b * (c ** 2 - (a ** 2) + (b ** 2) - (2 * a * b))) / 2
        return round(area, 2)
    else:
        return -1