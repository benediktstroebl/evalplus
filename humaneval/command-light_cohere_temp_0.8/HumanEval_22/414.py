```python
from typing import List
def filter_integers(values:
    """
    filtered_int: List[int] = []
    for value in values:
        if isinstance(value, int):
            filtered_int.append(value)
    return filtered_int
values = [1, 2, 'three', 3, 'four', 'five', seven]
print(filter_integers(values))  # Output: [1, 2, three, 5, seven]
``` 
This script defines a function **filter_integers** that filters a list of any Python values and only returns integers. The function iterates through each value in the input list, and checks if the value is an instance of the int class using the isinstance() function. If the value is an number, it is added to the **filtered_int** list.