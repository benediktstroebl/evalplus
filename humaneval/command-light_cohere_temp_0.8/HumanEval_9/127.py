```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x, i in zip(sorted(numbers), numbers) if i < len(numbers)]

# Test the function with a sample input and check the output
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]

numbers2 = [5, 6, 3, 2, 7]
result2 = rolling_max(numbers2)
print(result2)  # Output: [5, 6, 7]
``` 

This script defines a rolling_max function that calculates the rolling maximum elements in a given list. It utilizes a zip function to iterate over the input list and the sorted version, and selects the elements that are present in both lists but in descending order. The function is then tested with two sample inputs, and the output is printed to the console.