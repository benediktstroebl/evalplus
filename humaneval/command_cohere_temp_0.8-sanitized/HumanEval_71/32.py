def triangle_area(a, b, c):
    s = sum([a, b, c])
    if len(set(s)) == 2 or (s[0] < s[1] + s[2]) and (s[1] < s[0] + s[2]) and (s[2] < s[0] + s[1]):
        try:
            area = (a * b * math.sin(math.pi / 3)) / 2
            return round(area, 2)
        except TypeError:
            return -1
    else:
        return -1