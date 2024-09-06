```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This function uses a list comprehension to filter out even elements at odd indices from the input list `lst`. These elements are then summed using the `sum()` function and returned. 
The problem statement asks for the sum of these elements, instead of returning them as a list.