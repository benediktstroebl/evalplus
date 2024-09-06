Here is a self-contained Python script that solves the problem of finding the rolling maximum element in a list of integers:
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_count = 0
    current_max = numbers[0]
    max_elements = [current_max]

    for num in numbers[1:]:
        if num > current_max:
            current_max = num
        max_count += 1

    if max_count == len(numbers) - 1:
        max_elements.else maximum_value = max_elements[0]
    else:
        maximum_value = max(max_elements)
        for index, num in enumerate(max_elements):
            if num == maximum_value:
                maximum_value = max_elements[index]
                break
        max_elements = [maximum_value]

    return max_elements
```
This function takes a list of integers as input and returns a list of integers containing the maximum element found while rolling over the sequence. The function uses a efficient approach to minimize the number of iterations by keeping track of the maximum element found and its count.