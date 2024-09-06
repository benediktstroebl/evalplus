Here's a Python script with a self-contained function `is_prime` that solves the problem:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function checks if a given number is prime or not. It first checks if the number is less than 2, returning `False` if so. Then, it iterates from 2 up to the square root of the number, checking whether the number is divisible by any other number. If the number is divisible by any other number in this range, it returns `False`. However, if the number is not divisible by any number in this range, it returns `True`.

This algorithm is more efficient than the naive approach of checking all divisors up to the number's size, as it minimizes the number of iterations needed by only iterating up to the square root of the number. 

This function can be improved further, especially for larger inputs, but this basic implementation serves its purpose and would pass the provided tests. 
Here are some example uses:
```python
# In the Python session
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

This function provides a straightforward approach to checking primality that can be easily used elsewhere in Python. Grateful if you could let me know if I have addressed your query correctly! Let me know if you would like me to explain any part of the solution or provide further clarifications.