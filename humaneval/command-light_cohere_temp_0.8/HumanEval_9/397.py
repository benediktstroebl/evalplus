Here is a self-contained Python function that solves the problem of finding the rolling maximum elements in a list of integers:
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_so_far = numbers[0]
    max_ending = numbers[0]
    seen = [0] + numbers[1:]
    result = [0]

    for num in numbers[2:]:
        if num > max_ending:
            max_ending = num
        seen.add(num)
        if seen == numbers[0]:
            max_so_far = max_ending
        result.append(max_ending)

    return result
```
This function takes a list of integers as input and iteratively finds the maximum element in the list that has been seen so far, and adds it to the result list. 

The function then returns the list of rolling maximum elements.