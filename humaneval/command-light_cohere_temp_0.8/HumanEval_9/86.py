```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [max(numbers[i:]) for i in range(len(numbers))]]

numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # [1, 2, 3, 3, 3, 4, 4]
```
This function uses the Python list max function with an index from the end of the list, generating the rolling maximum element in the sequence.