def triangle_area(a, b, c):
    s = sum([a, b, c])
    if len(set(x + y for x, y in zip(a, b, c)) ) == 2 or (2 * max(a, b, c) >= s and 2 * min(a, b, c) <= s):
        return round(0.5 * (s * (s - a) * (s - b) * (s - c)) / (2 * s), 2)
    else:
        return -1