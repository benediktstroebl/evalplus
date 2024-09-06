```python
def multiply(a, b):
    num_a = str(a)
    num_b = str(b)
    p = 0
    for i in range(max(len(num_a), len(num_b))):
        if len(num_a) <= i:
            digit_a = 9
        else:
            digit_a = int(num_a[i])
        if len(num_b) <= i:
            digit_b = 9
        else:
            digit_b = int(num_b[i])
        p = (p + digit_a * digit_b) % 10
    return p
```

The script defines a Python function called `multiply` that takes two integer inputs, `a` and `b`. It calculates the product of the unit digits of `a` and `b` and returns the result. 

To do this, it first converts the inputs `a` and `b` to strings, and then iterates through the characters of the longer number, checking the corresponding digit in the other number at each position. It calculates the product of these digits and shifts the result by 10 to eliminateCarry, and repeats this process until the final result is in the range 0 to 9, which is the required product of the unit digits.

The function is designed to handle cases where the input numbers have different lengths gracefully, and it assumes that the input values are valid integers.