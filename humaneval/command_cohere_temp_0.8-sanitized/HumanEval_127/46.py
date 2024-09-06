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
    s = max(s1[0], s2[0]) - min(s1[0], s2[0]) + 1
    if s1[1] < s2[1]:
        s = max(s, s1[1] - s2[0] + 1)
    elif s2[1] < s1[1]:
        s = max(s, s2[1] - s1[0] + 1)
    if is_prime(s):
        return "YES"
    else:
        return "NO"