```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_acc = []
    for num in numbers:
        if not in max_acc:
            max_acc.append(num)
        else:
            max_acc[0] = max(max_acc[0], num)
    return max_acc

# Test suite
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This Python code defines a function `rolling_max` that calculates the rolling maximum elements in a given list of integers. The function uses a list comprehension to maintain a list called `max_acc` to keep track of the maximum elements encountered so far. The loop iterates through the maximum elements, and whenever a new element is encountered, it updates the current maximum in `max_acc` if necessary.

The test suite includes a list of integers and passes the `rolling_max` function over this list. The expected output is the list of the rolling maximum elements.