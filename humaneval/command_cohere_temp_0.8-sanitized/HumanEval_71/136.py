def triangle_area(a, b, c):
    s = sum([a, b, c])
    if len(set(s)) == 2 or (s[0] < s[1] + s[2]) and (s[1] < s[0] + s[2]) and (s[2] < s[0] + s[1]):
        try:
            return round((1.0 / 2) * (a * b * s[0] - a * c * s[1] + b * c * s[2]), 2)
        except ZeroDivisionError:
            return -1
    else:
        return -1