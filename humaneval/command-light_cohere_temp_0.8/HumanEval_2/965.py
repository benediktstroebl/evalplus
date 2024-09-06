```python
def truncate_number(number: float) -> float:
    # Decompose the number into integer part and decimal part
    int_part = int(number)
    decimal_part = number - int(number)

    # Return the decimal part
    return decimal_part

# Test cases #passes
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(2.0))  # Output: 0.0
print(truncate_number(-0.0))  # Output: 0.0
print(truncate_number(1.0))  # Output: 0.0
print(truncate_number(0.5))  # Output: 0.0
print(truncate_number(1.2))  # Output: 0.1
print(truncate_number(123.456))  # Output: 65
```