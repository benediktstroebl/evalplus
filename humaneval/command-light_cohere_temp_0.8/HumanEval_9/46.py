```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_so_far = numbers[0]
    max_ending = numbers[0]
    result = [max_so_far]
    for num in numbers[1:]:
        if num > max_ending:
            max_ending = num
        elif num == max_ending and num > max_so_far:
            max_so_far = num
    result.append(max_ending)
    return result

# Test cases
test_data = [1, 2, 3, 2, 3, 4, 2]
test_result = rolling_max(test_data)
print(test_result)
test_data = [2, 3, 4, 5]
test_result = rolling_max(test_data)
print(test_result)
``` 
This code defines a rolling maximum function that generates a list of rolling maximum elements in a given sequence. The function uses a array to keep track of the maximum element seen so far and the maximum element in the sequence. The test cases verify the test data.