def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1,  0)
def gcd(x: int, y: int) -> int:
    while y != 0:
        x, y = y, x % y
    return x