```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This function uses a list comprehension to filter out even integers from the list that are located at odd indices, and then returns their sum. 

Note that the function assumes that the list contains only integers, as this is the common case for lists of numbers; however, it may be desirable to enhance this function to handle potential non-numeric elements gracefully in a more general scenario.