```python
from typing import List

def filter_integers(values):
    """
    Filter given list of any python values only for integers.
    Args: values (List[Any]): Python list to be filtered.
    Returns: list of integers (List[int]).
    """
    return [num for num in values if isinstance(num, int)]

# Test case 1
values_test1 = ['a', 3.14, 5]
result_test1 = filter_integers(values_test1)
print(result_test1)

# Test case 2
values_test2 = [1, 2, 3, 'abc', {}, []]
result_test2 = filter_integers(values_test2)
print(result_test2)

# Test case 3
values_test3 = [3.14, "hello", 5]
result_test3 = filter_integers(values_test3)
print(result_test3)
```