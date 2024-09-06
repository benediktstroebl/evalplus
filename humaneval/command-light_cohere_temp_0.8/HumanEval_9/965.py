```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Returns a list of rolling max elements from the input list.
    """
    list of integers -> List[int]
    """
    return [num for num, i in zip(numbers, numbers + [0])][::-1][i % len(numbers)]

if __name__ == "__main__":
    numbers = [1, 2, 3, 2, 3, 4, 2]
    print(rolling_max(numbers))  # Output: [3, 3, 3, 4, 4]
``` 
The function `rolling_max` calculates the rolling max elements over a given input list of integers, and the `if __name__ == "__main__"` block ensures that the function is only executed when the script is run directly.