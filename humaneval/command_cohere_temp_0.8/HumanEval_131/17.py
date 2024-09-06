```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2:
            product *= int(digit)
    return product if product else 0
```

This function iterates through each digit in the decimal representation of the input integer `n`. It multiplies the `product` variable by each odd digit and accumulates the result. If all digits are even, it returns 0. The markdown code block illustrates a problem that the function correctly solves.