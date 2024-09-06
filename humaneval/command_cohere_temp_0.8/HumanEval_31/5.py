```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function checks if a given number is prime or not. It first checks if the given number is less than 2, returning false immediately if so. Then, it iterates from 2 up to the square root of the number, checking whether the number is divisible by any other number. If the number is divisible by any other number in this range, it returns false; otherwise, it returns true. 

This function is relatively efficient for checking primality, as the number of iterations is limited to the square root of the given number. This is important because some inefficient primality checks can take a very long time for large numbers. 

This approach is efficient enough for manual checks, but modern cryptographic applications may require tighter security properties in which primality is assured with even higher levels of certainty through more sophisticated algorithms. 

This function can be invoked with various test cases to validate its behavior:
```python
>>> is_prime(6)
False
>>> is_prime(101)
True
>>> is_prime(11)
True
>>> is_prime(13441)
True
>>> is_prime(61)
True
>>> is_prime(4)
False
>>> is_prime(1)
False
```

As with any code, it is advisable to test this function with many different inputs to confirm that it behaves as expected, given your specific use case.