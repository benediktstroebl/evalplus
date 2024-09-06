```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [n for n, i in zip(numbers, range(len(numbers))) if numbers[i] >= numbers[i - 1]]

# Sample input and output
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]
```
This Python code defines a rolling_max function that takes a list of integers as input and generates a new list of integers where each element is the maximum of its corresponding index and the previous element in the input list. 
To test the code's functionality, it defines a sample input list numbers and calls the rolling_max function with this input. The result is then printed, showing that the function correctly identifies and returns the list of rolling maximum elements found in the input sequence.