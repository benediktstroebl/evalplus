def triangle_area(a, b, c):
    s = (a + b + c) / 2  # semi-perimeter
    if s > max(a, b, c):
        return round(math.sqrt(s * (s - a) * (s - b) * (s - c)) / 2, 2)
    else:
        return -1