def triangle_area(a, b, c):
    s = sum(i for i in [a, b, c] if i < sum(j for j in [a, b, c] if j != i))
    if len(s) > 0:
        return round(0.5 * abs(sin(π * sum(i/j for i,j in zip(s, s+s)))), 2)
    else:
        return -1