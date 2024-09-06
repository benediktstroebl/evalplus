```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    numbers = set(numbers)  # Remove duplicates using set()
    return list(numbers)

# Example function call that demonstrates the expected output
test_remove_duplicates([1, 2, 3, 2, 4])
``` 
The function remove_duplicates, which accepts a list of integers and outputs a list of integers that have not been duplicated, is implemented in this script. The function uses the set() method to get rid of any duplicate numbers and then uses the list() constructor to turn the set back into a list.