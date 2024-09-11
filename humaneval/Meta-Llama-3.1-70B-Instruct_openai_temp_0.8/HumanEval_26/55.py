```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: The list with duplicates removed.

    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    seen = set()
    seen_twice = set()

    # Create a list of numbers we've seen so far to keep track of duplicates
    for num in numbers:
        if num in seen_twice:
            continue
        elif num in seen:
            seen_twice.add(num)
        else:
            seen.add(num)

    # Return the list of numbers that have not been seen before
    return [num for num in numbers if num not in seen_twice]


# Test the function
if __name__ == "__main__":
    print(remove_duplicates([1, 2, 3, 2, 4]))  # Expected output: [1, 3, 4]
    print(remove_duplicates([1, 1, 1, 1, 1]))  # Expected output: []
    print(remove_duplicates([1, 2, 3, 4, 5]))  # Expected output: [1, 2, 3, 4, 5]
```