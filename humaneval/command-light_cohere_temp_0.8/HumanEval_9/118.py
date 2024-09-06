```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum elements from a given list of integers.
    :return [sorted(numbers, reverse=True)[:moment]]
    """
    return sorted(numbers, reverse=True)[:moment]

# Example test cases
numbers1 = [1, 2, 3, 4, 5]
numbers2 = [6, 7, 8, 9, 10]
numbers3 = [4, 2, 8, 3, 10]

result1 = rolling_max(numbers1)
result2 = rolling_max(numbers2)
result3 = rolling_max(numbers3)

print("Result 1:", result1)
print("Result 2:", result2)
print("Result 3:", result3)
```
This code defines the `rolling_max` function that takes a list of integers as an argument and returns a list of the rolling maximum elements found until a given moment in the sequence. It uses the sorting the result in descending order and takes the first `moment` element as the threshold to generate the rolling maximum. 
The code then provides three test cases to demonstrate the function's behavior, and the results are printed to the console.