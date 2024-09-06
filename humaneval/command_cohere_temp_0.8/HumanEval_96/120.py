```python
def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n."""
    count = 0
    prime_numbers = []
    for num in range(2, n+1):
        if is_prime(num) and num < n:
            prime_numbers.append(num)
            count += 1
            if count == n:
                break
    return prime_numbers
```

This script defines a function `count_up_to()` that takes an integer `n` as input and returns an array of the first `n` prime numbers less than `n`. 

The `is_prime()` function is used to check if a number is prime. This function checks if the number is less than or equal to 1, in which case it immediately returns `False`. It then iterates through the numbers from 2 to the square root of the number and checks if the number is divisible by any of them. If it is, it returns `False`. If it isn't, it returns `True`. 

In the `count_up_to()` function, we then iterate through the numbers from 2 to `n` and check if it's prime with the `is_prime()` function. We also check if the number is less than `n` so we don't go past the `n` values requested. Once we find `n` prime numbers, we stop the list with `break`. 

Here is an example of how to use these functions:
```python
print(count_up_to(5)) # [2, 3]
print(count_up_to(11)) # [2, 3, 5, 7]
print(count_up_to(20)) # [2, 3, 5, 7, 11, 13, 17, 19]
```

This would print out the requested prime numbers up to the respective numbers.