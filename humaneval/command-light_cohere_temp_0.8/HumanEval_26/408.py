```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))
# Test the function
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print("List after removing duplicates:", result)

numbers2 = [1, 1, 2, 1, 3, 2]
result2 = remove_duplicates(numbers2)
print("List after removing duplicates:", result2)
```
This code introduces a method called `remove_duplicates` which accepts a list of integers and then returns a new list with all distinct integers. It utilizes the use of the set() function to create the new list, which automatically removes duplicate elements from the input list.

The code then applies this function to two different lists and prints out the resulting lists, demonstrating that duplicates have been successfully removed.