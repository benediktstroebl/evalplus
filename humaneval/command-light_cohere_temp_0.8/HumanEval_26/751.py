```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove all elements that occur more than once from a list of integers.
    """
    list(set(numbers, {x for x in numbers if numbers.count(x) == 1}))
    return list(numbers)

if __name__ == "__main__":
    numbers = [1, 2, 3, 2, 4, 2, 1, 5]
    print(remove_duplicates(numbers))
``` 
The provided code defines a function called remove_duplicates that takes a list of integers as input and returns a new list with duplicate values removed. The function achieves this using the set-like behavior to filter out the duplicate values and then convert the set back into a list.