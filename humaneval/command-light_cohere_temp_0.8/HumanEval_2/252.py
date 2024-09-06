```python
def truncate_number(n: float) -> float:
    # function to return integer part of a number
    i = n - 1
    while i > 0 and n % 10 == 0:
        i -= 1
    return i + n // 10

# test case
print(truncate_number(3.5))  # expected output: 2.0
print(truncate_number(10.5))  # expected output: 5.0
print(truncate_number(-1.5))  # expected output: 0.0
print(truncate_number(1e+6))  # expected output: 1e+6.0
print(truncate_number(1e+7))  # expected output: 1e+7.0
```

This Python code defines a function `truncate_number` that takes a number and returns its integer part. The function employs a formula to remove the decimal part from the number, which is the largest integer less than the given number, and then adds back the remainder (the decimal part) divided by 10. The function then tests the code by passing the test case of `3.5`, which should return `2.0`.  The print `10.5` which should return `5.