```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = [num for num in numbers if num not in seen]
    seen.add(numbers)
    return result

numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # expected output: [1, 3, 4]
``` 
This function uses a set to keep track of numbers seen so far, then iterates through the input list and adds each number to the set if it has not been encountered before. It then returns a