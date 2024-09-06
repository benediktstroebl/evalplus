def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def intersection(s1, s2):
    st, en = max(s1[0], s2[0]), min(s1[1], s2[1])
    if en - st + 1 < 2:
        return "NO"
    elif is_prime(en - st + 1):
        return "YES"
    else:
        return "NO"