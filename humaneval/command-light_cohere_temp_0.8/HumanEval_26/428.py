```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes elements that occur more than once from a list of integers.
    : Returns a list with all unique integers
    """
    numbers = set(numbers)  # Convert input list to a set to remove duplicates
    return [x for x in numbers if x not in numbers.

if __name__ == "__main__":
    numbers = [1, 2, 3, 2, 4, 3, 5]
    print("Unique elements:", remove_duplicates(numbers))
    ```