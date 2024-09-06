```python
from typing import List

def filter_integers(values:
    return [num for num in values if isinstance(num, int)]

# Test cases
values1 = [1, 2, 3, 'abc', }
values2 = [3.14, 5]
result1 = filter_integers(values1)
result2 = filter_integers(values2)

print("Test case 1: ", end="")
print(result1)
print("Test case 2: ", end="")
print(result2)
``` 
The function `filter_integers` takes a list of values and returns a new list containing only the integers from the input. The function uses the filter technique, which goes through the list of values and uses the `isinstance` function to filter out any values that are not instances of `int`.  The function then returns a new list containing only the integers from the input list.