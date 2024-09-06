def triangle_area(a, b, c):
    s = sum(a, b, c)
    if abs(s - max(s)) < 1e-5:
        return round(0.5 * (a * b * sin(π/3)) / (a + b + c), 2)
    else:
        return -1