```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This function uses a list comprehension to filter out even integers from the list that are located at odd indices, and then returns their sum. 

This should correspond to the examples in the prompt, as for the example `add([4, 2, 6, 7])` it should return `2`, which is the only even integer at an odd index in the list, and return it as a sum.