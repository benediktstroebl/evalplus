```python
from typing import List

def filter_integers(values: 
    return [num for num in values if isinstance(num, int)]
):
    pass

# Test the function with various inputs
values_test = [['a', 3.14, 5, 1, 2, 3, 'abc', {}, []]
print(filter_integers(values_test))  # Output: [5, 1, 2, 3]

```
This code defines a function called **filter_integers** that takes a list of values and returns a new list containing only the integers from the input. It uses the filter technique to filter elements based on their type, and the type of the elements in the list is checked using the **isinstance** method. 
This function is then tested with a list of values and the output is printed.