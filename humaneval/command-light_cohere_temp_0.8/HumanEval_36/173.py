```python
def fizz_buzz(n: int):
    count = 0
    for i in range(2, n+1):
        num = 0
        while 11 <= i and i % 13 == 0:
            num += 1
        if num == 7:
            count += 1
    return count

# Test the function
assert fizz_buzz(50) == 0
assert fizz_buzz(78) == 2
assert fizz_buzz(79) == 3

# This code provides a self-contained function and tests in a single script

Note: You can use this code as a starting point for your project and build upon it.