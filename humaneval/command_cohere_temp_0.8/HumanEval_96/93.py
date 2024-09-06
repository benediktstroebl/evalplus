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
    """Return an array of the first n prime numbers less than n"""
    count = 0
    numbers = []
    for num in range(2, n+1):
        if is_prime(num) and num < n:
            numbers.append(num)
            count += 1
            if count == n:
                break
    return numbers
```

This code defines two functions: `is_prime`, which checks whether a given number is prime, and `count_up_to`, which returns the first `n` prime numbers less than `n` and if `n` is less than or equal to 0, it returns an empty list. 

Here is an example of how to use the function:
```python
print(count_up_to(5))  # [2, 3]
print(count_up_to(11))  # [2, 3, 5, 7]
print(count_up_to(20))  # [2, 3, 5, 7, 11, 13, 17, 19]
print(count_up_to(0))  # []
print(count_up_to(1))  # []
print(count_up_to(18))  # [2, 3, 5, 7, 11, 13, 17]
```