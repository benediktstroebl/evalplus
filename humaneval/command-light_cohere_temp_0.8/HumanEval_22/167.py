```python
from typing import List

def filter_integers(values):
    """Filter given list of any python values only for integers"""
    return [num for num in values if isinstance(num, int)]

# Test cases
values1 = [1, 'a', 3, 'c', (])
values2 = [1, 2, 'three', (5), {}]
values3 = [1, 2, 3, 'abc', [1, 2]]

print("Test case 1: ", end="")
print(filter_integers(values1))
print("")

print("Test case 2: ", end="")
print(filter_integers(values2))
print("")

print("Test case 3: ", end=")")
print(filter_integers(values3))
``` 
This Python code defines a function called `filter_integers` that filters a list of any Python values, retaining only the integers. The function operates by converting each value to an integer using the `isinstance` method, and then appending it to the result list if the value is an integer. The code includes several test cases to verify the functionality of the `filter_integers` function, passing in different sets of values to ensure that it correctly filters out non-integer elements.