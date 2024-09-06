```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This function uses a list comprehension to filter out even elements at odd indices from the input list `lst`. These elements are then summed using the `sum` function. The function gracefully handles scenarios with no valid elements or a empty list, where it returns 0 and  0 respectively, as these cases are handled in the problem statement and corresponding tests.  This is tested against the provided examples and the test suite.