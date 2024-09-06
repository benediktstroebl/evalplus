```python
from typing import List

def filter_integers(values):
    """ Filter given list for integers only"""
    return [int(x) for x in values if x.isinstance(int)]

# Test cases
test_values1 = [1, 2, 'three', 3.14, 5]
test_values2 = [1, 2, 3, 'abc', {}, []]

print("Test case 1: ", end="")
print(filter_integers(test_values1))
print("\n")

print("Test case 2: ", end="")
print(filter_integers(test_values2))
print("\n")

```
This Python script defines a function named `filter_integers` that filters a given list of values and returns a new list containing only the integers. It uses the particular instance of the int() function to convert the string values to integers before filtering. The function is then tested with two test cases, and the results are printed to the console.