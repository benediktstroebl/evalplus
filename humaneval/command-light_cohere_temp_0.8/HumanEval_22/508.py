```python
from typing import List

def filter_integers(values:
    """
    filtered = [x for x in values if isinstance(x, int)]
    return filtered

# Test cases
test_values = [1, 2, 3, 'abc', float('3.14'), []]
test_filtered = filter_integers(test_values)

print("Test Values:", test_values)
print("Test Filtered:", test_filtered)

``` 
This code defines a function **filter_integers** that takes a list of values and returns a new list containing only the integers from the input. 
The function uses a list comprehension to filter the elements based on their type, specifically checking if they are instances of int. 

The function is then tested with several input values and the output is printed to the console.