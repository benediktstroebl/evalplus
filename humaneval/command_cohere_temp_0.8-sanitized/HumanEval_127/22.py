def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def intersection(s1, s2):
    s1_start, s1_end = s1
    s2_start, s2_end = s2
    if s1_end < s2_start or s2_end < s1_start:
        return "NO"
    else:
        intersection_start = max(s1_start, s2_start)
        intersection_end = min(s1_end, s2_end)
        intersection_length = intersection_end - intersection_start
        if is_prime(intersection_length):
            return "YES"
        else:
            return "NO"