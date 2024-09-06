```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [n for n, i in zip(numbers, range(len(numbers))) if i == numbers[i][1]]
    ```  This function uses the `zip` function to associate each element of the list with its position, and then iterates through the list using a generator expression to generate the rolling maximum element for each position in the list.