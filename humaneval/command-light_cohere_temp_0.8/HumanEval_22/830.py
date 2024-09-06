```python
from typing import List
def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

#Test cases
values_test = [1, 2, 3, 'abc', {}, [3, 4], 5]
print("Test case 1:", values_test)
print("Expected Output:", [1, 2, 3])

values_of_empty = []
print("Test case 2:", values_of_empty)
print("Expected Output:", [])

values_with_objects = [1, 2, 'apple', 3.14, (4)]
print("Test case 3:", values_with_objects)
print("Expected Output:", [1, 2, 3. value, int(3.14), 4])

values_not_int = ['a', 3.14, 5]
print("Test case 4:", values_not_int)
print("Expected Output:", [])
```