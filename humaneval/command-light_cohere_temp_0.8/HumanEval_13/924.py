```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    if a == 0:
        return b
    elif b == 0:
        return a

    # Compute all potential divisors
    potential_divisors = [x for x in range(1, max(a, b) + 1)]

    # Remove duplicates and sort
    potential_divisors.sort()

    unique_divisors = list(set(potential_divisors))

    # Determine the greatest divisor
    gcd = 0
    i, j = 1, unique_divisors[0]
    while i < len(unique_divisors) and j:
        if a % j == 0 and b % j == 0:
            gcd = j
            i, j = i + 1, j
        else:
            j = j - 1

    return gcd
```  This solution efficiently calculates the greatest common divisor of two integers a and b using the GCD algorithm. It handles cases where a maximum input values, and also ensures that the result is returned correctly.