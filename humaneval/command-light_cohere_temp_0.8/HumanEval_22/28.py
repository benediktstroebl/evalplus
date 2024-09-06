```python
from typing import List

def filter_integers(values:
    return [int(x) for x in values if type(x) == int]

# Test case 1
values1 = ['a', 3.14, 5]
result1 = filter_integers(values1)
print(result1)  # Output: [5]

# Test case 2
values2 = [1, 2, 3, 'abc', {}, []]
result2 = filter_integers(values2)
print(result2)  # Output: [1, 2, 3]

# Test case 3
values3 = [1, 2, 3, 4, 'five', 6]
result3 = filter_integers(values3)
print(result3)  # Output: [1, 2, 3, 4, 6]
```

The function `filter_integers` in this version takes a list of values as input and returns a new list that only contains integers. The function works by using a list comprehension with a condition that checks if each element in the input list is an integer.

The script also includes three test cases to demonstrate the function's behavior.