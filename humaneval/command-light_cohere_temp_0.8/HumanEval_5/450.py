```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list.
    :param numbers: list of integers
    :param delimiter: int
    :return: list of integers with the elements separated by the 'delimiter'.
    """
    # Ensure the list has at least element
    if len(numbers) == 0:
        return []

    # Insert the delimiter after the first and before the last element
    result = [numbers[0]] + [numbers[-1]] + [delimiter] + numbers[1:]
    return result

# Test cases
test_numbers = [1, 2, 3]
test_result = intersperse(test_numbers, 4)
print(test_result)  # Expected Output: [1, 4, 2, 4, 3]

test_empty_list = []
test_result_empty = intersperse(test_empty_list, 4)
print(test_result_empty)  # Expected Output: []

test_single_element = [1]
test_result_single = intersperse(test_single_element, 4)
print(test_result_single)  # Expected Output: [1, 4, 2, 4, 3]

test_list_with_empty = [1, 2, 3,]
test_result_empty_list = intersperse(test_list_with_empty, 4)
print(test_result_empty_list)  # Expected Output: [1, 2, 3]
```