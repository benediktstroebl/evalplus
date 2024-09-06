```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [max(numbers[i:i], numbers[i+1:j]) for i, j in enumerate(enumer)]

# Test cases
numbers1 = [1, 2, 3, 4]
numbers2 = [2, 3, 4, 5]

result1 = rolling_max(numbers1)
result2 = rolling_max(numbers2)

print("Result 1:", result1)
print("Result 2:", result2)
```

The function `rolling_max` takes a list of integers as input and returns a new list that contains the maximum element from the rolling window of the input sequence. 

The rolling window is determined by the two indices `i` and `j` that move through the list. 
At each step, the maximum element between the current element and the next element in the sequence is selected.