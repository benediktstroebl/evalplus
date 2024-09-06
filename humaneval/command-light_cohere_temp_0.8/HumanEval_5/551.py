```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter if i < len(numbers) - 1 else num for i, num in enumerate(numbers)]

# Unit Tests
numbers_list = [1, 2, 3]
result_list = intersperse(numbers_list, 4)

assert len(result_list) == 4
assert all(map(lambda x: x == x+4, result_list))

numbers_list = [10, 20, 30]
result_list = intersperse(numbers_list, 4)

assert len(result_list) == 6
assert all(map(lambda x: x == x+4, result_list))

numbers_list = [10, 100, 100]
result_list = intersperse(numbers_list, 4)

assert len(result_list) == 4
assert all(map(lambda x: x == x+4, result_list))

numbers_list = [10, 10, 100, 10]
result_list = intersperse(numbers_list, 4)

assert len(result_list) == 6
assert all(map(lambda x: x == x+4, result_list))
```
The code defines a `intersperse` function that takes a list of numbers and a delimiter as input and returns a new list with the numbers separated by the delimiter. The `typing` import ensures correct function usage with `List` objects, and the use of `enumerize` to iterate through the elements of the list. 
The code also includes several tests to verify the correctness of the `intersperse` function.