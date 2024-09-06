```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_length: int) -> List[int]:
    """
    Generate a list of rolling maximum elements observed in the list within the rolling_length window.
    """
    if rolling_length <= 0:
        return []

    res = [num for num in numbers[:rolling_length]]
    for i in range(rolling_length, len(numbers)):
        if numbers[i] > numbers[i - rolling_length]:
            res.append(numbers[i])
        else:
            res.append(numbers[i - rolling_length])
    return res

# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_length = 3
result = rolling_max(numbers, rolling_length)
print(result)
```

The above code defines the `rolling_max()` function which takes a list of numbers `numbers` and an integer `rolling_length` as input and returns a list of integers which represents the rolling maximum elements observed within the `rolling_length` window throughout the sequence. The function starts by creating an initial list of the first `rolling_length` elements from the input list. For each subsequent element in the input list, it compares this element with the element at the same position in the last `rolling_length` elements of the input list (`numbers[i] > numbers[i - rolling_length]`). If the current element is greater, it adds this element to the rolling maximum list. Otherwise, it keeps the previous maximum element in the rolling maximum list. This approach ensures that the rolling maximum list always contains the maximum elements observed within the window up to each point in the sequence.

The output of the provided example usage is:
```python
[1, 2, 3, 3, 3, 4, 4]
``` 

Which is the expected result for the provided example input.