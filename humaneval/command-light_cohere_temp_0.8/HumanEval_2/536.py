```python
def truncate_number(n: float) -> float:
    if n < 0:  # Numbers less than 0 will have no decimal part
        return n
    elif n == 1:  # Special case: only one decimal, which is 0
        return 0.0
    else:  # Otherwise, n is greater than 1
        return round(n)
```
This Python code defines a function called `truncate_number` that takes a floating-point number `n` as input and returns the decimal part of the number. The function performs the`n if `n` is less than 0, it has no decimal part, and it returns `n` as is. Otherwise, it checks if `n` is equal to 1, which is a special case where the number has only one decimal part, returning 0.0. If `n class Simultaneously, let's discuss the function further.