```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This function uses a list comprehension to filter out even integers from the list that are located at odd indices, and then returns their sum. 

Note that the function assumes that the list contains only integers, as the `%` operator is used to determine even or oddness. If the list contains other data types, the function may not provide the expected result. 

If this assumption does not hold for the problem you are given, please clarify the requirements of the function so I can adjust my solution to it.