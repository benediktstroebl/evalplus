def intersection(interval1, interval2):
    s1, e1 = interval1
    s2, e2 = interval2
    return "YES" if max(s1, s2) < e1 + 1 and s2 < e1 else "NO"