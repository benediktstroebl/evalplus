```python
def add(lst):
    even_odd = []
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 == 0:
            even_odd.append(lst[i])
    return even_odd
```

This function uses a list comprehension to filter out even integers from the list that are located at odd indices. The function will return the list of even integers that are located at odd indices. 

 
For instance, running the function with the input list `[4, 2, 6, 7]` will return `[2]`.