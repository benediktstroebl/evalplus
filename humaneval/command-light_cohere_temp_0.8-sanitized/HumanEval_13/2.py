def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    else:
        return max(a % d for d in range(1, min(a, b) + 1))