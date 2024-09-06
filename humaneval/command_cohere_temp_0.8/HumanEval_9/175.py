Here's a Python script that contains a function called `rolling_max` which takes a list of integers `numbers` as input and returns a list of rolling maximum elements found up to that point in the sequence:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    max_so_far = numbers[0]
    max_found = [max_so_far]
    
    for num in numbers[1:]:
        if num > max_so_far:
            max_found.append(num)
            max_so_far = num
    
    return max_found

# Test cases
numbers_test_cases = [
    [1, 2, 3, 2, 3, 4, 2],
    [1],
    [1, -1],
    [0, 0, 0, 1, 0, 2, 1, 1, 1, 0, 1, 2, 2],
    [12, 12, 15, 2, 10, 12, 13, 11, 12],
]

for numbers in numbers_test_cases:
    solution = rolling_max(numbers)
    print(f"== Original ({len(numbers)})\n{numbers}\n== Solution\n{solution}\n")
```

This script uses a rolling maximum variable `max_so_far` to keep track of the maximum element found thus far. Initially, it's set to the first element of the list. The function then iterates through the list, comparing each element to the `max_so_far`, and updates both `max_so_far` and the `max_found` list if the current element is greater. The final output is a list of all rolling maximum elements found up to each point in the sequence.

The script also includes test cases to validate the function against different scenarios.