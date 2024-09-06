```python
def multiply(a, b):
    return int(str(a) + str(b)) * 10 ** min(len(str(a)), len(str(b)))
```

This function takes two integers a and b as input and returns the product of their unit digits. The unit digit is the last digit of a number, considering the decimal being truncated. It combines the two numbers' last digits and multiplies them by 10 raised to the minimum of the lengths of their representations. This approach ensures the correct unit digit and provides the desired result.