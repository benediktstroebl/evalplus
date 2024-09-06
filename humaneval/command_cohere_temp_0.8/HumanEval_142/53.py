```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            num **= 2
        elif i % 4 == 0 and i % 3 != 0:
            num **= 3
        result += num
    return result
```
The function sums over the list, updating each list element value according to its index modulos 3 and 4, then returning the total. 

This solution employs a simple loop accumulating the sum, determining each element's value by its index' modulos 3 and 4. Employing Python's enumerate improves readability, especially when querying nested lists. This results in a clean, efficient, and tested solution.