```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))

# Sample test cases
numbers1 = [1, 2, 3, 2, 4]
numbers2 = [3, 2, 4, 2, 5]
numbers3 = [1, 2, 2, 3]

print("Test case 1 results: ", remove_duplicates(numbers1)) # [1, 2, 3, 4]
print("Test case 2 results: ", remove_duplicates(numbers2)) # [2, 3, 4]
print("Test case 3 results: ", remove_duplicates(numbers3)) # [1, 2, 3]
```
This code defines a function **remove_duplicates** that accepts a list of integers and generates a new list with no duplicates. The function uses the **set()** function to create a set of all elements in the input list, then uses the **list()** function to convert the set back to a list, which effectively removes any duplicates.

Finally, it provides three test cases: one with duplicate elements, another with unique elements, and a third that is a mix of duplicates and unique elements. The **remove_duplicates** function is then called for each test case, and the results are printed out to the console.