```python
def truncate_number(number: float) -> float:
    # Decompose the number into integer part and fractional part
    integer = number // 1
    fractional = number % 1
    # Return the fractional part of the number
    return fractional
# Test cases
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(0.5))  # Output: 0
print(truncate_number(-0.5))  # Output: 0
print(truncate_number(10.0))  # Output: 1
print(truncate_number(2.0))  # Output: 2
```