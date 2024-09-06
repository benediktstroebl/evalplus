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

This script defines a function called `sum_squares` taking a list of integers as an input and returning the required sum. The function enforces the criteria for squaring or cubing the integers based on the index as requested in the problem statement. While being mindful of the given examples, the function handles an empty list case as well.