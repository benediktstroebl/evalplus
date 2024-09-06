```python
from typing import List
def remove_duplicates(numbers: List[int]):
    # Initialize an empty set to store unique integers
    duplicates = set()
    result = []

    # Iterate through the input list
    for num in numbers:
        if num not in duplicates:
            duplicates.add(num)
            result.append(num)

    return result

# Test cases
test_list1 = [1, 2, 3, 2, 4]
test_list2 = [4, 2, 3, 1, 5]
test_list3 = [1, 2, 2, 4, 3]

# Call the function and assert the results
assert(remove_duplicates(test_list1) == [1, 3, 4])

assert(remove_duplicates(test_list2) == [4, 2, 3])

assert(remove_duplicates(test_list3) == [1, 2, 2, 4])
```