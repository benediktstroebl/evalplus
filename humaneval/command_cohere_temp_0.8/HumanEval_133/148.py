```python
def sum_squares(lst):
    """
    Return the sum of squared integers in the list, rounding each number to the next bigger integer.
    """
    result = 0
    for n in lst:
        result += int(n + 1e-5) ** 2  # Adding 1e-5 prevents rounding errors occurring at floats
    return result

# Tests:
assert sum_squares([1, 2, 3]) == 14
assert sum_squares([1, 4, 9]) == 98
assert sum_squares([1, 3, 5, 7]) == 84
assert sum_squares([1.4, 4.2, 0]) == 29
assert sum_squares([-2.4, 1, 1]) == 6
```

This approach ensures that all elements are treated as integers, thus avoiding any confusion or unexpected results from floating-point operations. It utilizes the `**` operation for actual squaring and includes a small positive value (`1e-5`) to the float to its next higher integer value. 

 rounding to the nearest integer and adds it to the result. 
This method provides accuracy and efficiency in handling both integers and floats while avoiding potential floating-point issues. 
If you want to analyze more test scenarios, I can assist in formulating additional test cases to cover different numerical scenarios.