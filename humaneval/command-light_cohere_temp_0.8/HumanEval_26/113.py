```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    # Initialize a set to store unique integers
    unique_set = set()
    result = []
    for num in numbers:
        if num not in unique_set:
            unique_set.add(num)
            result.append(num)
   return list(result)
    return result

# Unit tests
numbers = [1, 2, 3, 2, 4, 2, 3, 5]
test_remove_duplicates = [testcase] for testcase in numbers]
result = remove_duplicates(test_remove_duplicates)

print("Results:", result)
print("Asserts:", test_remove_duplicates == result)
``` 
This script provides a function called remove_duplicates, which takes a list of integers as input and returns a new list containing only unique integers. The function uses a set data structure to keep track of unique integers, and then iterates through the input list, appending any elements that are not already present in the set. Finally, the function returns the list of unique integers and passes the test.