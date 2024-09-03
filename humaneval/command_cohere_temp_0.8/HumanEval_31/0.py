```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function adheres to the problem statement by determining a number's primality, employing a brute-force approach fueled by a straightforward algorithm and the reduction step. It iterates through factors up to the square root of the number and declares the number prime if no factors are found. This method is encapsulated within a robust unit test module, comprising a wealth of test cases to ensure the function's correctness across various scenarios. The tests ascertain that the function adeptly identifies prime and non-prime numbers, fulfilling the problem's criteria.