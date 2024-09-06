def triangle_area(a, b, c):
    s = sum(a, b, c)
    if s == a + b or s == b + c or s == c + a:
        area = (a * b * (c * (c - a) * (c - b) / ((s - a) * (s - b) * s))) / 6
        return round(area, 2)
    else:
        return -1