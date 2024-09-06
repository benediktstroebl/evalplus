def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def intersection(s1, s2):
    x = max(s1[1], s2[1]) - min(s1[0], s2[0])
    if x <= 0:
        return "NO"
    if is_prime(x):
        return "YES"
    else:
        return "NO"