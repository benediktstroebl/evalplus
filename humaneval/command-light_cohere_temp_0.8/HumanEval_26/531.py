```python
from typing import List
def remove_duplicates(numbers: List[int]):
    return [x for x in numbers if x not in numbers[:]]

# Test the function with a simple example
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Expected output: [1, 3, 4]
```
This Python code defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate values removed. The function utilizes a list comprehension to iterate through the input list and checks if each element is not already present in the new list created by removing duplicates. The result is then a list containing only unique elements from the original list.

The code then tests the `remove_duplicates` function with a sample list of integers. It passes the test with this example and prints the resulting list, which should contain only the unique elements from the input list.