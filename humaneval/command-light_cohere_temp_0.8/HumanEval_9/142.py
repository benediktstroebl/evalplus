```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    numbers = [num for num in numbers if num > 0]  # Filter out negative numbers
    max_index = numbers.max_num = max(numbers)
    rolling_max = [num for i, num in enumerate(numbers) if num == max_num][max_index]
    return rolling_max

# Test case
test_numbers = [1, 2, 3, 4, 3, 2, 1]
test_result = rolling_max(test_numbers)
print(test_result)

```
In this script, the rolling_max function accepts a list of integers as input and returns a new list containing the rolling maximum element from the input sequence. It uses the time out to ensure that only positive numbers remain in the input list, then finds the maximum number and selects the corresponding element from the list to be the rolling maximum. The test case demonstrates how the's the function by passing a test list and prints the resulting list.