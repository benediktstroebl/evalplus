```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This function uses a list comprehension to filter out even integers from the list that are located at odd indices, and then returns their sum. 

The test cases are written in a way that verifies both the oddness of the index and the evenness of the element at that index. 

For example, the list `[4, 2, 6, 7]` would return `2`, since the even integer `2` is at an odd index `1`.  Another example, with the list `[1, 3, 5, 7, 2, 4]` would also return `2`, since the even integers on the list are `2` and `4`, located at indices `3` and `5` respectively.  These are consistent with the examples provided in the prompt.