Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function checks if a given number is prime or not. It first checks if the given number is less than 2, returning False if so. It then iterates from 2 up to the square root of the number, checking whether the number is divisible by any other number. If the number is divisible by any other number in this range, it returns False. However, if the number is not prime, it returns True.

Here is a markdown code block with corresponding test cases to verify its correctness:
```python
# Test cases
assert is_prime(6) == False, "Test case 1 failed"
assert is_prime(101) == True, "Test case 2 failed"
assert is_prime(11) == True, "Test case 3 failed"
assert is_prime(13441) == True, "Test case 4 failed"
assert is_prime(61) == True, "Test case 5 failed"
assert is_prime(4) == False, "Test case 6 failed"
assert is_prime(1) == False, "Test case 7 failed"
```

You can copy and paste this code block into a Python interpreter or script to test the correctness of the `is_prime` function.