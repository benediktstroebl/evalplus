def triangle_area(a, b, c):
    s = (a + b + c) / 2  # semi-perimeter
    if s >= a and s >= b and s >= c:
        area = (a * b * sin(180 / 3 - arcsin(s / a))
                + b * c * sin(180 / 3 - arcsin(s / b))
                + c * a * sin(180 / 3 - arcsin(s / c)))
        return round(area, 2)
    else:
        return -1