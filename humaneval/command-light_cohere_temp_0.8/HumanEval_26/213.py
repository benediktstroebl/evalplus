```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [num for num in numbers if num not in seen and num not in numbers[seen]]
 
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Expected output: [1, 3, 4]
```
This function takes a list of integers as input and returns a new list with all the integers that are not duplicates and not already present in the input list. The function utilizes a implementation using a set data structure to keep track of seen integers and removes duplicates. The final output will be a list with the duplicate integers removed.