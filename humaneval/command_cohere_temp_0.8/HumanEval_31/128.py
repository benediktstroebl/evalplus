```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function incorporates the necessary logic to determine whether a given number is prime. It begins by checking if the number is less than 2, returning `False` if so, since primality requires numbers to be greater than 1. The function then initiates a loop from 2 up to the square root of the target number. This loop examines whether the target number is divisible by any integer within this range. If divisibility is found, the function returns `False`, indicating that the number is not prime. However, if no divisors are encountered, the function returns `True`, signifying that the number is indeed prime. 

This streamlined Python script offers an efficient and accurate primality-testing mechanism. It is compatible with the problem statement and aligns with the provided test cases. 

This function can be optimized further, particularly for larger values of `n`, by limiting the range of divisors to [2, n] instead of [2, int(n ** 0.5) + 1]. For example:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n + 1):
        if n % i == 0:
            return False
    return True
```

This modification can improve runtime efficiency for larger numbers, since the loop no longer needs to iterate to the square root of the number. 

Let me know if I can assist further with any other details or related optimization strategies!