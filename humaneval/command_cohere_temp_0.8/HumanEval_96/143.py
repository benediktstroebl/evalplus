Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
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

The `count_up_to()` function iterates through numbers from 2 up to `n`, adding each prime number to the `prime_numbers` list until the list reaches a length of `n`. 

You can test the `is_prime()` function and `count_up_to()` function with the following tests:
```python
# Test is_prime()
print(is_prime(0))      # Output: False
print(is_prime(1))      # Output: False
print(is_prime(2))      # Output: True
print(is_prime(3))      # Output: True
print(is_prime(4))      # Output: False
print(is_prime(5))      # Output: True
print(is_prime(6))      # Output: False

# Test count_up_to()
print(count_up_to(5))     # Output: [2, 3]
print(count_up_to(11))    # Output: [2, 3, 5, 7]
print(count_up_to(0))     # Output: []
print(count_up_to(20))    # Output: [2, 3, 5, 7, 11, 13, 17, 19]
print(count_up_to(1))     # Output: []
print(count_up_to(18))    # Output: [2, 3, 5, 7, 11, 13, 17]
```

Note that the `is_prime()` function utilizes an optimized strategy for primality testing, which checks only the divisibility of a number up to its square root. This is much more efficient than looping through every number up to the target number.