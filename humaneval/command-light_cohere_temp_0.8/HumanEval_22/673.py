```python
from typing import List
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test cases
values_test_cases = [
    [],  # [] converts to empty list
    ['a'],  # String, not int
    3,  # Integer
    [1, 2, 'abc'],  # Mixed list with int and non-integer elements
]

print("Test Cases:", values_test_cases)
print()

for values in values_test_cases:
    print(filter_integers(values))
```
The above Python script defines a function `filter_integers` that filters out any non-integer values from a given list. It uses list comprehension to iterate through the elements of the input list and checks if each element is an instance of the integer class using the isinstance() function. The filtered list of integers is then returned. 

The script also provides a set of test cases to verify the behavior of the function. Finally, the test cases are printed to the console.