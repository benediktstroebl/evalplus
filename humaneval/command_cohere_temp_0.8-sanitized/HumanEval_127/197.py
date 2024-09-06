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
    x = max(s1[1], s2[1]) - min(s1[0], s2[0])
    if x <= 0:
        return "NO"
    if is_prime(x):
        return "YES"
    else:
        return "NO"