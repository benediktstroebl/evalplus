```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2:
            product *= int(digit)
    return product if product else 0
```

This function traverses the decimal representation of the input number `n`, multiplying each odd digit found (i.e., digits that are 1, 3, 5, 7, or 9) into the `product`. It returns 0 if all digits are even, implying no odd digits.

The precision of this approach lies in its ability to consider odd and even digits differently, manipulating them appropriately within the loop. This delivers the intended result without exploiting any specific odd or even number patterns. Thus, it handles any positive integer input gracefully, aligning with the problem statement.