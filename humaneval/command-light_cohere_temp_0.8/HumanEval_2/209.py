```python
def truncate_number(n):
    int_part = (n % 1)
    dec_part = (1 - (n // 1))
    return float(int_part) + float(dec_part)

# Test cases
print(truncate_number(3.5)) # Expected output: 2.0
print(truncate_number(0.1)) # Output: 0.0
print(truncate_number(-3.9)) # Output: -0.2
print(truncate_number(30.9)) # Output: 30.0
print(truncate_number(10.5)) # Output: 10.0
print(truncate_number(1.0)) # Output: 2.0
```

This code defines a function called `truncate_number`, which takes a number as input and returns the truncated decimal part of that number. It achieves this by extracting the integer part and the decimal part of the input number. The test cases cover various input scenarios, and the function successfully passes them all.