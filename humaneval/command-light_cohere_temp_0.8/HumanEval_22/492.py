```python
from typing import List

def filter_integers(values):
    return [int(el) for el in values if type(el) == int]

# Test case 1
values1 = ['a', 3.14, 5]
result1 = filter_integers(values1)
print(result1)  # Output: [5]

# Test case 2
values2 = [1, 2, 3, 'abc', {}, []]
result2 = filter_integers(values2)
print(result2)  # Output: [1, 2, 3]

# Test case 3
values3 = [1, 2, 3, []]
result3 = filter_integers(values3)
print(result3)  # Output: [1, 2, 3]
```

The provided code includes a function called `filter_integers` that takes a list of values as an argument. It then returns a filter the values that are integers using list comprehension and the `type` check. The code includes three test cases:
1. Test case 1: The function is called with a list of values, and the output is a list containing only the integer '5'.
2. Test case 2: The function is called with a list of values, and the output is a list containing only the integers '1', '2', and '3'.
3. Test case 3: The function is called with a list of values that contain a string and an empty list, and the output is a list containing only the integers '1', '2', and '3'.