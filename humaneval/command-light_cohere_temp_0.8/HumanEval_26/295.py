```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in set(numbers)]

# Example test cases
numbers1 = [1, 2, 3, 2]
numbers2 = [1, 2, 3, 4, 2, 3]
numbers3 = [3, 2, 1, 4]

print("Results of numbers1: ", end="")
remove_duplicates(numbers1)
print()
print("Results of numbers2: ", end="")
remove_duplicates(numbers2)
print()
print("Results of numbers3: ", end="")
remove_duplicates(numbers3)
```
The `remove_duplicates` function receives a list of integers and returns a new list with all distinct integers from the input. The function utilizes the testing and a set data structure to identify duplicate integers and remove them from the input list.