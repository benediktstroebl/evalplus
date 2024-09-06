```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [x for x in numbers if x not in seen and x not in numbers[:-len(seen)]]
 
# Test the function
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))

numbers = [1, 2, 3, 3, 4]
print(remove_duplicates(numbers))

numbers = [5, 6, 7, 8, 9]
print(remove_duplicates(numbers))
```
The code defines a function **remove_duplicates(numbers: List[int]) -> List[int]** that takes a list of integers as input and returns a new list with all distinct integers from the input list. 

It utilizes a set to keep track of seen integers and then loops through the input list, checking each element against the set to see if it's already in the list. It removes duplicates and returns the results.