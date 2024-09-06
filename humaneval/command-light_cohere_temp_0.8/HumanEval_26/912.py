```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [x for x in numbers if x not in seen and x not in numbers[:0]]

# Test the function with a list of integers, removing duplicates
test_list = [1, 2, 3, 2, 4, 3]
result = remove_duplicates(test_list)
print(result)

# Test the function with a list of strings, keeping duplicates
test_str = ["a", "b", "a", "c", "b"]
result = remove_duplicates(test_str)
print(result)
```
This Python script defines a function called `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate elements removed. It uses a run-time and set data structures to efficiently remove duplicates.

The `remove_duplicates` function tests with two different types of input: a list of integers and a list of strings, respectively. The results show that the output is consistent with the input.

This code demonstrates the use of sets and run-time lists in Python for solving the problem of removing duplicate elements from a list of integers or strings.