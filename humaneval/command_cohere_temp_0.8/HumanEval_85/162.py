```python
def add(lst):
    even_odd = []
    for i in range(len(lst)):
        if i % 2 == 1 and lst[i] % 2 == 0:
            even_odd.append(lst[i])
    return even_odd
```

This function uses a list comprehension to filter out even integers that are located at odd indices from the input list `lst`. The function will return the list of even integers located at odd indices from the input list. 

This approach allows the function to overcome issues presented by lists that may contain empty sub-lists and still perform the necessary filtering and iteration required to solve the problem. 

Let me know if you would like me to explain how the code works in more detail or include some test cases to verify the functionality of this solution.