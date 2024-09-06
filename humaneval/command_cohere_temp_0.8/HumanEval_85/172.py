```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This function uses a list comprehension to filter out even elements at odd indices from the input list `lst`. These elements are then summed using the `sum()` function and returned. 

Would you like to know more about the functionality of the code? Or would you like to troubleshoot potential issues in the code? Feel free to ask any specific questions or requests, and I will do my best to help you!