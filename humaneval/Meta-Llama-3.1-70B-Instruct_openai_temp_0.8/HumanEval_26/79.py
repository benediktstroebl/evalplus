```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    :param numbers: A list of integers
    :return: A list of integers with duplicates removed
    """
    seen = set()  # To keep track of elements we've seen so far
    seen_multiple = set()  # To keep track of elements that occur more than once
    result = []  # The resulting list with duplicates removed

    for num in numbers:
        if num in seen_multiple:
            continue
        elif num in seen:
            seen_multiple.add(num)
            # If we've seen this number before, remove it from the result
            result = [x for x in result if x!= num]
        else:
            seen.add(num)
            result.append(num)

    return result

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```
This script works by iterating through the input list and keeping track of the elements it has seen so far. When an element is encountered for the second time, it is added to the `seen_multiple` set, which causes it to be removed from the result. The result is then returned as a list of integers with duplicates removed.