Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function returns true if the given number is prime, and false otherwise. It first checks if the given number is less than 2, returning false if so. It then iterates from 2 up to the square root of the given number, checking whether the given number is divisible by any of these numbers. If the number is divisible by any of them, it returns false. If it is not, it returns true.

Here's a markdown code block with the function and some tests to verify its behavior:
```python
# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Tests
assert is_prime(6) == False
assert is_prime(101) == True
assert is_prime(11) == True
assert is_prime(13441) == True
assert is_prime(61) == True
assert is_prime(4) == False
assert is_prime(1) == False
```

The tests correspond to the example tests provided earlier, and the function's behavior is illustrated by these tests. 

The logic employed by this function is the same as that in the provided example. It begins by determining whether the given number is lesser than 2, at which point it returns false. It then iterates through numbers from 2 up to the square root of the given number, checking whether the given number is divisible by any of them. If it is, it returns false. If it is not, it returns true.  This approach is efficient because it only requires checking divisibility for numbers up to the square root of the given number. 

Let me know if this solution works for you or if you have any other questions!