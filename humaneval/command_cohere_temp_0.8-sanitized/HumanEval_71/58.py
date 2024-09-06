def triangle_area(a, b, c):
    s = sum(i for i in [a, b, c] if i < sum(j for j in [a, b, c] if j != i))
    if s == 3:
        return -1
    else:
        return round(0.5 * (a * b * scipy.gamma(1/2)) / (math.sqrt(2 * math.pi)), 2)