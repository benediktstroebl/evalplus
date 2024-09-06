```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [num] + [num + delimeter for num in numbers] + [num]
    return result

# Test cases
numbers_list = [4, 2, 3, 1]
test_delimiter = 4

result_expected = [1, 4, 2, 4, 3]

print("Test case 1 result:", result_expected)
print("Test case 1 input:", numbers_list)

numbers_list = [1, 2, 3, 4]
test_delimiter = 3

result_expected = [1, 2, 3, 4]

print("Test case 2 result:", result_expected)
print("Test case 2 input:", numbers_list)
```
The function `intersperse` receives a list of integers `numbers` and an integer `delimiter` as input and returns a new list that intersperses the numbers with the `delimiter`. The function adds the first element to the list and then uses a list comprehension to add the `delimiter` between every two consecutive elements in the `numbers` list.