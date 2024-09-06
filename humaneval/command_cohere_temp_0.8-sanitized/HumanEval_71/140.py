def triangle_area(a, b, c):
    s = (a + b + c) / 2  # semi-perimeter
    if s >= a and s >= b and s >= c:
        area = (a * b * c) / 2
        return round(area, 2)
    else:
        return -1