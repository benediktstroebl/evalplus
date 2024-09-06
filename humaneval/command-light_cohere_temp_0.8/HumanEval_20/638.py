```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    SELECTS AND RETURNS TWO NUMBERS THAT ARE CLOSEST TO EACH OTHER
    AND RETURN THEM IN ORDER OF SMALLER NUMBERS, LARGER NUMBERS.
    FROM A SUPPLED LIST OF NUMBERS (OF LENGTH AT LEAST TWO)
    SELECT two_numbers = (numbers[0] + numbers[1]) / 2, numbers[0] + numbers[1])
    if two_numbers < numbers[0] + numbers[1]:
        return (numbers[0], two_numbers)
    return (numbers[0], numbers[1])

Tests:
>>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2])
2.0, 1.0]

[1.0, 3.0, 4.0, 2]
```