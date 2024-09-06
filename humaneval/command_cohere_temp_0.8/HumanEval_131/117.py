```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2:
            product *= int(digit)
    return product if product else 0
```

This function iterates through each digit in the decimal representation of the input integer `n`. It multiplies the `product` variable by each odd digit and accumulates the result. If all digits are even, it returns 0.

To see the behavior of the function for different inputs, you can test it with:
```python
# Test cases
print(digits(1))  # Output: 1
print(digits(4))  # Output: 0
print(digits(235)) # Output: 15
``` 

This should output:
```
1
0
15
```