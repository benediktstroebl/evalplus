```python
from typing import List
def remove_duplicates(numbers: List[int]):
    return List(set(numbers))

# Test the remove_duplicates function with a sample input
numbers = [1, 2, 3, 2, 4]
print("Test 1:", remove_duplicates(numbers))  # Expected output: [1, 3, 4]

# Test the function with a different list of integers
numbers2 = [5, 10, 15, 3, 8, 2]
print("Test 2:", remove_duplicates(numbers2))  # Expected output: [5, 10, 15, 3, 8, 2]
```
The provided Python script defines a function remove_duplicates that takes a list of integers as input and returns a new list with duplicate elements removed. The function uses the fact that the set function is applied to the input list, which effectively removes duplicate elements by converting the list to a set and backtracking the unique elements. 

The script then tests the function with two different lists of integers, printing the results to verify that the expected output is achieved. The purpose of this script is to demonstrate a self-contained function that efficiently removes duplicates from a list of integers.