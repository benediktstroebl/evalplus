def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
def intersection(s1, s2):
    s = max(s1[1], s2[1]) - min(s1[0], s2[0])
    if s == 0 or not is_prime(s):
        return "NO"
    return "YES"