def triangle_area(a, b, c):
    s = sum(a, b, c)
    if abs(s - max(s, key=s.count)) < 1e-5:
        return round(0.5 * (s * (s-a) * (s-b) * (s-c)) ** 0.5, 2)
    else:
        return -1