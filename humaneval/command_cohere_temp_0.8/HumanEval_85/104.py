```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This function uses a list comprehension to filter out even elements at odd indices from the input list `lst`. These elements are then summed using the `sum` function. The function gracefully handles cases where the input list is empty or doesn't contain any even elements at odd indices by returning 0. It also has the advantage of not modifying the original list `lst` and instead returns the sum directly.  This aligns with the principle of least surprise and helps ensure clarity and efficiency in solving the problem.