```python
def add(lst):
    even_odd = [val for i, val in enumerate(lst) if i % 2 == 1 and val % 2 == 0]
    return sum(even_odd)
```
This function uses a list comprehension to filter out even integers from the list that are located at odd indices, and then returns their sum. 

Note that this function assumes that the list contains only integers and that there is at least one even integer located at an odd index in the list. If the list does not meet these conditions, the function may not return the expected results.