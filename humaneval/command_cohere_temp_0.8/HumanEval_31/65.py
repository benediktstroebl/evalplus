```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function `is_prime` takes an integer `n` as input and checks if it is prime or not. It employs a straightforward algorithm that iterates through the integers from 2 up to the square root of `n`, checking whether `n` is divisible by any of them. If `n` is divisible by any of these integers, it returns `False`, indicating that `n` is not prime. However, if `n` survives the iteration without finding a divisor, it returns `True`, indicating that `n` is prime. 

This algorithm has a time complexity of O(√n), meaning that it checks approximately `n` squared integers to determine if it is prime. While this is a relatively efficient method for checking primality, there are other algorithms with superior performance in certain situations, such as the `Sieve of Eratosthenes` for larger ranges.  But the `is_prime` function provides a straightforward and intuitive way to check for primality in many real-world cases.