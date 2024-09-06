```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This function uses a list comprehension to filter out even integers from the list that are located at odd indices, and then returns their sum. 

Note that this function assumes that the list contains only integers, as the `%` operator is used to determine even or oddness. If the list contains other data types, the function may not return as expected. 

Let me know if this resolves the problem you had or if you'd like me to provide any additional clarifications or examples on how to iterate and solve mathematical problems like this one.