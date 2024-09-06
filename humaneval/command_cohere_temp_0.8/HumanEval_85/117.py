```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This function uses a list comprehension to filter out even elements at odd indices from the input list and then returns their sum. Note that the function assumes that the list contains only integers and doesn't handle other data types. If the input list contains elements of other data types or needs to be handled more carefully, additional error handling and validation might be necessary.