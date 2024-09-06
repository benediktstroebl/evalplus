```python
def largest_divisor(n: int) -> int:
    return n // max(n, 1)

# Test case 1
assert largest_divisor(15) == 5

# Test case 2
assert largest_divisor(6) == 2

# Test case 3
assert largest_divisor(0) == 0

# Test case 4
assert largest_divisor(-10) == -1
``` 
The code defines a function `largest_divisor` which returns the largest integer divisor of the input number 'n'. The function uses the max function to find the maximum integer less than the input number that divides the input number evenly.  The max function returns the max value that is smaller than the input number and evenly divides it.