```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This function uses a list comprehension to filter out even elements at odd indices from the input list `lst`. These elements are then summed using the `sum` function. The result is the sum of all the even elements at odd indices in the input list. 

This solution effectively solves the problem as outlined in the markdown code block and maintains code clarity and efficiency. 

Let me know if you would like to further discuss the solution or delve into any details!