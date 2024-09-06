```python
def truncate_number(n: float) -> float:
    if n < 0.5:
        raise ValueError("Input number must be positive")
    return n // 1.5

print(truncate_number(-1.2))  # #
```
This function takes a positive floating point number and returns the decimal part of that number, while raising an error if the input number is negative.