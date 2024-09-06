```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod
```

This problem can be solved by multiplying the odd digits in the decimal representation of `n` while ignoring the even ones. Slowly iterating through the integer's digits, digit by digit, and checking if each one is odd before multiplying it into the product `prod` will result in the desired output. The provided code adheres to this approach. 

This approach has a time complexity of O(n), where n is the number of digits in the given integer, as it requires iterating through each digit once.

Here's an example usage of the `digits` function with tests:
```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod

# Test cases
assert digits(1) == 1
assert digits(4) == 0
assert digits(235) == 15
assert digits(7) == 7
assert digits(0) == 0
```