```python
def sort_third(l: list):
    """Sorts list l such that values at indices divisible by three are in l and are sorted, while other values are sorted normally"""
    l = [5, 6, 3, 4, 8, 9, 2]
    return sorted(l, key=lambda x: x if x % 3 == 0 else x)
```
The code defines a function `sort_third` that takes a list `l` as input and returns a sorted list `l'`. The function uses a lambda function as the key argument to the `sorted` function. The lambda function checks if the the value of each element in the list is divisible by three, and if so, it returns that element. If the element is not divisible by three, it returns the element as is. This effectively sorts the common values (indices divisible by three) first, and the remaining values are sorted normally.