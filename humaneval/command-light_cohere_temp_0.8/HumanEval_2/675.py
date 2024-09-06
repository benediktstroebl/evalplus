Here's the solution:
```python
def truncate_number(n: float) -> float:
    # split the number into an integer and a decimal part
    int_part = n // 1
    decimal_part = n % 1
    # return the decimal part
    return decimal_part

# test cases
print(truncate_number(3.5))  # expected output 0.5
print(truncate_number(0.0))  # expected output 0.0
print(truncate_number(-3.5))  # expected output - decimal part is always smaller than 1, so it won't cause an error
print(truncate_number('3.5'))  # expected output 0.0
print(truncate_number(10.2))  # expected output 0.2
print(truncate_number(0.999))  # expected output 0.999
```

This Python function, `truncate_number`, takes a number as input and returns the decimal part of that number. It works by splitting the number into an integer part and a decimal part, and then returning the decimal part of the number.