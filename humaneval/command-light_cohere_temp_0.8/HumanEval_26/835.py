```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = [num for num in numbers if num not in seen]
    seen.add(numbers)
    return result

numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))
``` 
This function removes duplicate numbers from the given list of integers. It utilizes a set to keep track of seen numbers, then iterates through the input list and adds numbers to the set if they are not already present. The output is the list with numbers without duplicates.