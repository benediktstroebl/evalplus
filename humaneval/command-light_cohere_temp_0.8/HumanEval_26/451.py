```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return theresult

# Input validation and sample test cases
numbers = [1, 2, 3, 2,4]
print("Input numbers:", numbers)
print("Result:", result)

numbers = [1, 2, 3, 2, 4, 2]
print("Input numbers:", numbers)
print("Result:", result)

numbers = [1, 3, 4, 2, 5, 6]
print("Input numbers:", numbers)
print("Result:", result)
```
This script defines a function called remove_duplicates that takes a list of integers as input and returns a new list with duplicate elements removed. The script uses a set to keep track of seen elements and then iterates through the input list, adding elements to the result list if they are not already present in the seen set. The function then returns the result.