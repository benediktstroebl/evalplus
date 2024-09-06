```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers. = sorted(numbers)
    rolling_max = []
    while True:
        current = numbers[0]
        for num in numbers[1:]:
            if current < num:
                current = num
        rolling_max.append(current)
        break
    return rolling_max

# Test case 1: [1, 2, 3, 2, 3, 4, 2]
test_case_1 = rolling_max([1, 2, 3, 2, 3, 4, 2])
print(test_case_1)

# Test case 2: [1, 2, 3, 3, 4, 4]
test_case_2 = rolling_max([1, 2, 3, 3, 4, 4])
print(test_case_2)

# Test case 3: [10, 20, 30, 40, 30, 20, 10]
test_case_3 = rolling_max([10, 20, 30, 40, 30, 20, 10])
print(test_case_3)
``` 
This Python code defines a function `rolling_max` that calculates the rolling maximum elements from a given list of integers. It uses a technique of sorting the list and iteratively selecting the maximum element from the sorted portion. Three test cases are generate lists with different integer sequences and then call the `rolling_max` function to verify its functionality. 

The output will display the rolling maximum elements for each test case.