```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0
    if a == 0:
        return b
    if b == 0:
        return a

    # Counted and tested items
    count_a = 0
    count_b = 0

    while a >= 1:
        count_a += 1
        a //= 2  # Integer division
    while b >= 1:
        count_b += 1
        b //= 2  # Integer division

    # Calculate gcd using the counts and minimal count
    gcd = min(count_a, count_b) + 1

    return gcd
```  This code defines a function greatest_common_divisor that computes the greatest common divisor of 2 integers a and b. The code uses the test a simple algorithm that iteratively divides the larger of the 2 numbers by 2 until the smaller one and keeps track of how many times you've done this.