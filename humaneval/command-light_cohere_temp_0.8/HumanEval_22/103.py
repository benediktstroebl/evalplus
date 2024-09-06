```python
from typing import List
def filter_integers(values:
    results = []
    for val in values:
        if isinstance(val, (int, float)):
            results.append(val)
    return results

# Example usage:
values = [1, 2, 3, 'abc', {}, []]
result = filter_integers(values)
print(result)
``` 
This code defines a function called **filter_integers** that takes a list of values as input and returns a new list containing only the integers from the input list.  The outputs the example usage demonstrates how to call the function with a sample list of values and print the resulting filtered list.