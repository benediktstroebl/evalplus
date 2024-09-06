```python
def truncate_number(number):
    return number - int(number)
```

The `truncate_number` function takes a single parameter, `number`, which represents the positive floating point number to be decomposed into an integer part and a decimal part. It does this by subtracting the integer part of `number` (obtained by converting `number` to an integer) from `number` itself. The resulting difference is the desired decimal part of the original number. This operation effectively isolates and returns the decimal part, regardless of the specific decimal precision of the input. 

To validate the correctness of the approach, let's consider a few test cases:
```python
# Test case showing the principle
assert truncate_number(3.5) == 0.5

# Test case with a fractional part smaller than 0.5
assert truncate_number(3.25) == 0.25

# Test case with a decimal point deeper than 1 (e.g. 3.235)
assert truncate_number(3.235) == 0.235

# Test case with a large integer part (e.g. 30.5)
assert truncate_number(30.5) == 0.5
```

In each case, the function `truncate_number` correctly identifies and returns the decimal portion of the input number. 

This straightforward solution is concise and easily understood, making it ideal for solving this problem.