```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x, y in zip(numbers, numbers[1:]) if y > x]

# Test cases
test_cases = [
    [1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4],
    [1, 2, 3, 4, 5, 6],
    [0, 1, 0, 2, 3, 4, 3, 4, 3]
]

results = {}
for test_case in test_cases:
    results[test_case] = rolling_max(test_case)

for result, test_case in zip(results.values(), test_cases):
    print(f"Expected: {test_case}, Got: {result}")
```  This code defines a function called rolling_max that takes a list of integers as input and returns a new list containing the rolling maximum elements in the original list. 

It utilizes the zip function to pair each element in the original list with the corresponding element from the list produced one element behind, and then selects the larger element through comparison. 

It then creates a test case dictionary with various input lists, and loops through these test cases, using the rolling_max function to get the expected results, and then compares these results with the actual results using the zip function.