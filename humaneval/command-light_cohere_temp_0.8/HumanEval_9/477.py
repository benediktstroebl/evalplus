```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, index in sorted((index, num) for index, num in enumerate(numbers))][1: :]

# Test cases
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Expected output: [1, 2, 3, 3, 3, 4, 4]

numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
result = rolling_max(numbers)
print(result)  # Expected output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

numbers = [5, 2, 1]
result = rolling_max(numbers)
print(result)  # Expected output: []
``` 
This solution defines a rolling_max function that uses the sorted function to get the index of the maximum element and then returns the maximum element for each moment in the sequence. The test cases demonstrate the each scenario and the expected output is printed to the console.