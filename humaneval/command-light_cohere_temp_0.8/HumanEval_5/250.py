```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test cases
test_data = [([1, 2, 3], 4), [10, 20, 30], [60, 40, 50])

def test_function(data):
    result = intersperse(data[0], data[1])
    expected = [1, 4, 2, 4, 3, 10, 20, 30]
    return result == expected

test_result = test_function(test_data)

if test_result:
    print("Tests passed!")
else:
    print("Tests failed.")
```

The function `intersperse` is designed to take two lists as input and return a new list where every second element is separated by a specified `delimiter`. The provided test cases demonstrate the expected behavior of the function when used with different lists.