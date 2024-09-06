```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod
```

This problem can be solved by iterating through each digit in the decimal representation of the number `n`. Using the modulo operator (`%`) it's possible to determine if a digit is odd or even. Subsequently, the product is incremented by the odd factor for the final result. 

This solution adheres to the given Markdown specification and accepts the problem statement tests. Let me know if further clarification is necessary.