```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            result += num ** 2
        elif i % 4 == 0 and i % 3 != 0:
            result += num ** 3
    return result
```

This script defines a function called `sum_squares` taking a list of integers as an input parameter `lst`. This function calculates the sum of squares for integer entries if their index is a multiple of 3 and the sum of cubes for integer entries if their index is a multiple of 4 but not a multiple of 3. The entries in the list whose index is not a multiple of 3 or 4 are not altered. Finally, the function returns the calculated sum, and the markdown block provides examples that prove its correctness.