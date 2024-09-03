def largest_divisor(n: int) -> int:
    return n // max(x for x in range(1, n+1) if x % n == 0)