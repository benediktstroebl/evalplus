```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This function uses a list comprehension to filter out even integers from the list that are located at odd indices, and then returns their sum. 

Note that this function assumes that the list contains only integers and that there is at least one even integer located at an odd index in the list. If the input list meets these assumptions, the function will produce the correct sum. 

This solution goes straight to the point and provides a simple answer to the problem without any brainstorming in the commentary. Let me know if you would like me to elaborate any further or provide additional coding insights.