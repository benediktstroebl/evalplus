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
    s1_end = max(s1[1], s2[1])
    s2_start = min(s1[0], s2[0])
    if s1_end < s2_start:
        return "NO"
    length = s2_start - s1_end
    if length == 0:
        return "YES"
    return "NO" if not is_prime(length) else "YES"