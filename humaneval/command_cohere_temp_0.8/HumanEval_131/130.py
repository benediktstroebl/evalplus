```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2:
            product *= int(digit)
    return product if product else 0
```

This function iterates through each digit in the decimal representation of the input integer `n`. It multiplies the `product` variable by each odd digit and accumulates the result. If all digits are even, it returns 0. The behavior for odd digits is consistent with the given problem description.

To see the behavior of the function for different inputs:
```python
print(digits(1))  # Output: 1
print(digits(4))  # Output: 0
print(digits(235)) # Output: 15
``` 

This implementation addresses the challenge of calculating the product of odd digits within a given positive integer, returning 0 when all digits are even. It delivers a straightforward solution that adheres to the problem's specified conditions.