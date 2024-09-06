```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This function uses a list comprehension to filter out even elements at odd indices from the input list and then uses the sum function to add these numbers. 
The function is also tested with the following test case to ensure its correctness:
```python
assert add([4, 2, 6, 7]) == 2
```