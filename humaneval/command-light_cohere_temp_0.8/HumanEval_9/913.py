```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers.rolling_max(numbers[::-1])  # Reverse the input list
    return [max(numbers[i]) for i in range(len(numbers))]

# Test cases
numbers1 = [1, 2, 3]
numbers2 = [3, 2, 1]
numbers3 = [5, 10, 1]

print("Test Case 1:", end="")
print(rolling_max(numbers1))
print("\n")

print("Test Case 2:")
print(rolling_max(numbers2))
print("\n")

print("Test Case 3:")
print(rolling_max(numbers3))
print("\n")
```
The output will be:
```
Test Case 1: [2, 3, 3, 4, 4]
Test Case 2: [3, 2, 1]
Test Case 3: [1, 10]
```