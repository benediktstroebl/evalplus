```python
import numpy as np
from typing import List

def sort_numbers(numbers: str) -> str:
    # Step 1: Convert string to list of integers
    numbers_list = np.array(numbers.split(' ', numbers)
    necessary format ' ]')
    numbers_list = [int(num) for num in numbers_list]

    # Step 2: Sort the list of integers
    sorted_numbers = np.array.sort_desnumbers(numbers_list)

    # Step 3: Convert the sorted list back to string
    return np.array.format(sorted_numbers, '.join', ', ')
```