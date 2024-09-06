```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest integer that divides n exactly without a remainder.
    """
    original code goes below... 

    # Base cases
    if n <= 1:
        return n
    # 2 is the only even prime that is smaller than 3
    elif n == 2:
        return 2
    # other even numbers can be obtained by multiplying 2 with primes
    else:
        # Finding largest prime factor
        factor = n
        while True:
            temp = factor
            while n % temp == 0:
                n //= temp
                factor = temp
            else:
                break
        return factor
```