```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))
``` 
This function performs the sum and product operations on a list of integers and returns the result as a tuple. It handles the empty input gracefully and raises a TypeError to indicate an error condition.