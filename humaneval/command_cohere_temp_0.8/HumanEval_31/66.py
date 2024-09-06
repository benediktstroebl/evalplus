```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function adheres to the problem statement by determining a number's primality, employing a brute-force approach fortified by the `range` function to iterate upwards from 2 to the square root of the number. When the number is divisible by any integer within this range, it is deemed composite and thus not prime. If no such divisor is found after having iterated through the entire range, the number is prime, hence the function returns `True`.

The edge cases (`n < 2`, `n == 1`, and `n == 4`) have been accounted for, and the function behaves as expected, aligning with the provided test cases. To achieve optimal performance for this practical problem, consider optimizing the brute-force approach, especially when dealing with larger numbers.