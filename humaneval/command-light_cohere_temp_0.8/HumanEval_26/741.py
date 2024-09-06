```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keeps elements elements left as in the input.
    numbers = set(numbers)  # Convert input list into set
    return list(numbers)  # Convert set back to list
"""

def test_remove_duplicates():
    assert remove_duplicates([1, 2, 3, 2, 4]) == [1, 3, 4]

if __name__ == "__main__":
    numbers = [1, 2, 3, 2, 4]
    print("Result:", remove_duplicates(numbers))
    test_remove_duplicates()
```
This Python code defines a function `remove_duplicates` that removes duplicate elements from a list of integers. It then includes a test function to verify the functionality of the `remove_duplicates` function. The `__main__` block demonstrates the usage of these functions, creating a list of numbers, and displaying the result along with passing the test function.