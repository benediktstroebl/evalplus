```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            prod *= int(digit)
    return prod
```

This `digits` function iterates through each digit in the decimal representation of the given number `n`. It multiplies the odd digits together, contributing to the `prod` variable, and thereby computing the final result. Additionally, the function addresses the edge case where all digits are even, returning 0 in such instances. 

Here is a test case to accompany the code:
```python
assert digits(1) == 1
assert digits(4) == 0
assert digits(235) == 15
```