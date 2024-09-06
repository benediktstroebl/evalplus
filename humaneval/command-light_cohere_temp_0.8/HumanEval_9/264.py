```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers = list(numbers)  # Convert input to list
    max_element = numbers[0]
    for num in numbers[1:]:
        if num > max_element:
            max_element = num
    return [max_element]

# Test cases
test_cases = [
    [1, 2, 3],
    [1, 3, 4, 2, 5],
    [10, 20, 30],
    [5, 10, 20, 15]
]

test_results = []
for test_case in test_cases:
    result = rolling_max(test_case)
    test_results.append(result)

print("Test results: ", test_results)
```
This Python code defines a function called rolling_max that calculates and returns the maximum element from a given list of integers. It utilizes the manual conversion of input to a list, and then iterates through the list to find the maximum element using the max() function. The test cases section contains a list of input lists, and the code calculates and stores the results for each test case in a new list called test_results. The results are then printed to the console.