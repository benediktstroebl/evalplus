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
    s1_end = s1[1]
    s2_start = s2[0]
    if s1_end < s2_start:
        return "NO"
    if s2_start > s1_end:
        return "NO"
    intersection_length = abs(s1_end - s2_start)
    if not is_prime(intersection_length):
        return "NO"
    return "YES"