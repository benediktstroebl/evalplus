def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def intersection(s1, s2):
    s1, s2 = min(s1), min(s2)
    e1, e2 = max(s1), max(s2)
    if s1 > e2 or s2 > e1:
        return "NO"
    length = e1 - s1 + 1
    if length == 1 or length == length // 2:
        return "NO"
    if is_prime(length):
        return "YES"
    else:
        return "NO"