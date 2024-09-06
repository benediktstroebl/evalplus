```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = [num for num in numbers if num not in seen and num > 0]
    seen.add(num)
    return result

# Add test cases here
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Expected output: [1, 3, 4]
``` 
This function, `remove_duplicates`, takes a list of integers as input and returns a new list with integers greater than 0. The function uses a set to keep track of integers that have been encountered before, and then it iterates through the input list, checking each element against the set. The function then adds elements to the set if the element is not previously encountered and is greater than 0.