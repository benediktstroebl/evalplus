```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [x for x in numbers if x not in seen and x not in numbers[numbers.keys()] and not in seen]

# Test the function
numbers = [1, 2, 3, 2, 4, 1, 3]
print(remove_duplicates(numbers))  # expected output: [1, 3, 4]
``` 
This function takes a list of integers and returns a new list with all the integers only once, along with their original order. This is is a way to solve the problem, which is to remove duplicate elements from a list and return the list with unique elements.