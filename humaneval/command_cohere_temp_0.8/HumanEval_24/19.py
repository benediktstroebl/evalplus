```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            j = n // i  # largest divisor
            return j if j < i else i
    return 1  # return 1 if no number divides n evenly
```

The function iterates through all numbers from 1 to n. If both the divisor and the quotient are larger than the current largest divisor, the function returns the divisor. 
If the divisor is larger and the quotient is not, the function returns the quotient. The function returns 1 if no divisor is found. This code solves the problem efficiently in O(n) time.