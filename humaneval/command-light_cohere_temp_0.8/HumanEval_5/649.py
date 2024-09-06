```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i+delimiter for i,j in zip(numbers,numbers[1:])+[delimiter]]

# Test case: empty input list
test_empty_list = intersperse([], 4)
print(test_empty_list)  # Expected output: []

# Test case: single element list
test_single_element = intersperse([1], 4)
print(test_single_element)  # Expected output: [1, 1, 2, 1, 3, 1]

# Test case: list of 2 elements
test_two_elements = intersperse([1,2], 4)
print(test_two_elements)  # Expected output: [1, 4, 2, 4, 3]

# Test case: list of 3 elements
test_three_elements = intersperse([1,2,3], 4)
print(test_three_elements)  # Expected output: [1, 4, 2, 4, 3, 4, 3]

# Test case: list of more than 3 elements
test_list_more_than_three = [1,2,3,4,5,6]
print(test_list_more_than_three)  # Expected output: [1, 4, 2, 4, 3, 4, 5, 6]
```

The function `intersperse` receives a list of numbers and a delimiter as input, and it uses a list comprehension to iterate over the input list twice, adding the delimiter as a separator between every two elements in the list. The resulting list contains the