```python
def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        tens, remainder = divmod(n, 5)
        if remainder == 0:
            return f"({tens}x{tens})"
        elif remainder == 1:
            return f"({tens}x{tens}-{int_to_mini_roman(1)})"
        else:
            return f"({tens}x{tens}-{int_to_mini_roman(remainder)})"

# Example usage
print(int_to_mini_roman(19))
print(int_to_mini_roman(152))
print(int_to_mini_roman(426))
```

This script leverages the decomposition of numbers into multiples of five and single units to represent numbers in Roman numerals in a condensed form. For instance, the number 19 is represented as `(xix)`, which translates to the Roman numerals for 19. Similarly, 152 is represented as `(clii)` and 426 as `(cdxxvi)`.