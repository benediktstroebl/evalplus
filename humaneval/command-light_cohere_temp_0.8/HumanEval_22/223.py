```python
from typing import List
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test cases
values_test_case1 = ['a', 3.14, 5]
assert filter_integers(values_test_case1) == [5]

values_test_case2 = [1, 2, 3, 'abc', {}, [5]]
assert filter_integers(values_test_case2) == [1, 2, 3]

values_test_case3 = [1, 2, 3, 4, 5, 'abc', None]
assert filter_integers(values_test_case3) == [1, 2, 3, 4, 5]

# Example usage
my_list = [1, 2, 3, 'abc', 4, 5]
result = filter_integers(my_list)
print(result)
```
This script defines a function called **filter_integers** that filters a list of values, passing the output to the assert statements for testing and an example usage of the function.

The function iterates through each element in the list and checks if it's an instance of the int class, returning only the elements that are integers. 
The script also provides test cases to validate the function's behavior.