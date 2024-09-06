```python
from typing import List

def filter_integers(values):
    """ Filter given list for integers only"""
    return [num for num in values if isinstance(num, int)]

# Test cases
test_values = [['a', 3.14, 5], [1, 2, 'abc', }, []]
test_results = filter_integers(test_values)

print("Test Results:", test_results)

# Sample Usage
my_list = [1, 2, 3, 'abc', {}, ]
final_list = filter_integers(my_list)
print("My List:", final_list)
```