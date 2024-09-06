```python
def add(lst):
    even_odd = [val for i, val in enumerate(lst) if i % 2 == 1 and val % 2 == 0]
    return sum(even_odd)
```

This function uses a list comprehension to filter out even integers from the input list that are located at odd indices, and then returns their sum. The problem scenario provided examples that coincide with the function's capabilities. Enjoy them as needed.