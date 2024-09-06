```python
from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    max_seen = numbers[0]
    result = [max_seen] * len(numbers)
    for i in range(1, len(numbers)):
        max_seen = max(numbers[i], max_seen)
        result[i] = max_seen
    return result
```

This Python script defines a function called `rolling_max` that uses a list of integers (`List[int])` as an input and returns a list of rolling maximum elements found in the sequence up to that point. It starts with the first element of the list as the maximum and maintains this rolling maximum as it iterates through the list, updating it whenever a larger element is encountered. The function essentially computes `[1, 2, 3, 3, 3, 4, 4]` as the output for the test case `[1, 2, 3, 2, 3, 4, 2]`.  The logic behind this approach is like this: 

1. Start with the first element in the list as the current maximum (`max_seen = numbers[0]`).
2. Iterate through the list, starting from the second element. For each element, compare it to the current maximum (`max_seen = max(numbers[i], max_seen)`).
3. If the current element is greater than the current maximum, update the maximum to the current element.
4. After iterating through the entire list, the `result` list will contain the rolling maximum elements, and this will be returned.

The function results in a list of the same length as the input list, with each element being the maximum for the corresponding window over the input sequence. 

This solution is efficient because it uses just one loop to traverse the list, making it linear time with respect to the list's size. It utilizes Python's maximum comparison operator (`max()`) to perform the rolling calculation in an efficient and concise manner.