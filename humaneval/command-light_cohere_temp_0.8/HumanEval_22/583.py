```python
from typing import List

def filter_integers(values):
    """ Filter given list of any python values only for integers."""
    return [i for i in values if isinstance(i, int)]

# Test cases
test_values = [['a', 3.14, 5], [1, 2, 'abc', {}, []]
test_results = filter_integers(test_values)

print("Test case 1:", end=")** (test_results)
print()
print("Test case 2:", end=")** (test_results)

# Output:
Test case 1:[5]

Test case 2:[1, 2, 'abc', []]
```
This Python script defines a function called **filter_integers** that filters a given list of values and returns a new list containing only the integers from the input. The function uses a list comprehension to achieve this. It checks if each value in the input list is an instance of the int class. The output of this script will be displayed in the console.