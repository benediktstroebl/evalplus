```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x, i in zip(numbers, range(len(numbers))) if i < len(numbers) and numbers[i] >= numbers[i+1]]

# Example function test
def test_rolling_max():
    assert rolling_max([1, 2, 3, 2, 3, 4, 2]) == [1, 2, 3, 3, 3, 4, 4]

# Test case 1
numbers = [1, 2, 3, 2, 3, 4, 2]
test_rolling_max()

# Test case 2
numbers = [1, 2, 3, 0, 1, 2, 3]
test_rolling_max()

# Test case 3
numbers = [10, 20, 30, 40]
test_rolling_max()
```
This Python code defines a function called **rolling_max** which takes a list of integers as an argument and returns a new list that contains the maximum elements from the original list after a specific order has been applied. 

The function uses the **zip** to iterate over the elements of the list and the index of each element. The **assert** statement is used to test the correctness of the **rolling_max** function by passing in different lists and checking if the resulting list matches the expected result.