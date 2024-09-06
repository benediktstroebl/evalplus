def triangle_area(a, b, c):
    s = sum([a, b, c])
    if len(set(s)) == 2 or (s[0] < s[1] + s[2]) and (s[1] < s[0] + s[2]) and (s[2] < s[0] + s[1]):
        ar = (a * b * (s[0] - a) * (s[1] - b) * (c - s[2]) / 96)
        return round(ar, 2)
    else:
        return -1