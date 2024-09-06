```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [max(numbers[i:i]) for i, n in enumerate(numbers)]
numbers = [1, 2, 3, 2, 3, 4, 2]
print(f"Rolling max: {', '.join(rolling_max(numbers))}")
```
This function utilizes the List comprehension technique to create a new list that contains the maximum value from the previous list, creating the rolling effect. The function then accepts a list of integers and uses the max function to find the maximum value in each list index.