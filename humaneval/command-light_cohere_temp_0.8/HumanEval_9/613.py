```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x, i in zip(numbers, range(len(numbers)))][::-1][numbers.count(max(numbers))]

# Unit tests
numbers = [1, 2, 3, 2, 3, 4, 2]
assert rolling_max(numbers) == [1, 2, 3, 3, 3, 4, 4]
numbers = [10,9,8,7,6,5,4,3,2,1]
assert rolling_max(numbers) == [10,8,7,6,5,4,3,2]
numbers = [9,2,6,5,3,4,8,7,6,5]
assert rolling_max(numbers) == [9,6,5,4,8,7,6]
```
This Python script presents a method called `rolling_max`, designed to produce a list of rolling maximum elements within a given list of integers. The function employs a count of the maximum value within the sequence as a proxy to the index of the rolling maximum. This method also utilizes a array slicing and the reversed sequence to obtain the rolling maximum elements.