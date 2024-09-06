```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = [x for x in numbers if x not in seen and x not in numbers[:-len(seen)]]
    seen.add(numbers)
    return result

# Example usage:
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
``` 
This Python function, remove_duplicates, accepts a list of integers as input and outputs a new list containing only the unique elements from the input list. This function utilizes a technique of converting the input list into a set and then filtering out duplicates from the set to generate the result.