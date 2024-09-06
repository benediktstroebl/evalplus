```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [max(numbers[i:], numbers[i+1]) for i in range(len(numbers)-1)]

# Test cases
numbers1 = [1, 2, 3, 4, 5]
should_max = rolling_max(numbers1)
print("Test case 1: ", end="")
print(should_max)

numbers2 = [1, 2, 2, 3, 4, 5]
should_max2 = rolling_max(numbers2)
print("\Test case 2: ", end="")
print(should_max2)

numbers3 = [1, 2, 3, 4, 6]
should_max3 = rolling_max(numbers3)
print("\Test case 3: ", end="")
print(should_max3)

numbers4 = [2, 1, 3, 4, 3]
should_max4 = rolling_max(numbers4)
print("\Test case 4: ", end="")
print(should_max4)
```
The code defines a function called rolling_max that takes a list of integers as input and returns a new list containing the maximum of consecutive elements in the input list. 

The code then provides several test cases to demonstrate the functionality of the rolling_max function.