```python
from typing import List
def filter_integers(values): 
    return [x for x in values if isinstance(x, int)]

# Test the function with known correct results
values1 = [1, 2, 3, 'abc', 5, 6, 'f']
values2 = [3, 'four', '67', 7]
values3 = [8, 9, 10]

print("Values 1: ", values1)
print("Filtered values 1: ", filter_integers(values1))

print("Values 2: ", values2)
print("Filtered values 2: ", filter_integers(values2))

print("Values 3: ", values3)
print("Filtered values 3: ", filter_integers(values3))
```
The function `filter_integers` is a self-contained Python function that filters a list of any Python values for integers. It uses the simple Python list comprehension to filter the values and returns a new list of integers.