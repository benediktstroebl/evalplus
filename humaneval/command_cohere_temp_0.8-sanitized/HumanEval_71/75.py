def triangle_area(a, b, c):
    s = sum([a, b, c])
    if len(set(s)) == 2 or (s[0] + s[1]) > s[2] and (s[0] + s[2]) > s[1] and (s[1] + s[2]) > s[0]:
        area = (a * b * (s[0] + s[1] + s[2]) / 2)
        return round(area, 2)
    else:
        return -1