```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    numbers = list(numbers)  # Convert the input list to an array
    max_element = numbers[0]
    current_element = max_element
    for num in numbers[1:]:
        if num > current_element:
            current_element = num
    return [current_element]

# Unit tests
numbers_test_data = [1, 2, 3, 2, 3, 4, 2]
expected_result = [1, 2, 3, 3, 3, 4, 4]
test_rolling_max(numbers_test_data)

int_list_test_data = [1, 2, 3, 4, 5]
expected_result = [1, 2, 3, 4]
test_rolling_max(int_list_test_data)

buffer_test_data = [1, 2, 3, 4, 3, 4, 5]
expected_result = [1, 3, 4, 4]
test_rolling_max(buffer_test_data)

custom_list_test_data = [2, 4, 5, 3, 6, 5]
expected_result = [2, 4, 5, 5]
test_rolling_max(custom_list_test_data)
```

In this Python code, the `rolling_max` function accepts a list of integers and outputs a list of the elements that are the maximum as the function loops through the list. The test cases include passing the example data and comparing the result with the expected output.