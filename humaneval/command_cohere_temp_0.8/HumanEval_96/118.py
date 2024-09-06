```python
def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n."""
    count = 0
    numbers = []
    for num in range(2, n):
        if is_prime(num) and num < n:
            numbers.append(num)
            count += 1
            if count == n:
                break
    return numbers
```

This script defines the `count_up_to()` function, which accepts a non-negative integer `n` and constructs an array of the first `n` prime numbers that are smaller than `n`. It also has a utility function `is_prime()` which is used to check if a number is prime or not. 

You can test this function by calling it with different inputs to verify the correctness of the result. 
For example:
```python
print(count_up_to(5)) # [2,3]
print(count_up_to(11)) # [2,3,5,7]
print(count_up_to(20)) # [2,3,5,7,11,13,17,19]
```