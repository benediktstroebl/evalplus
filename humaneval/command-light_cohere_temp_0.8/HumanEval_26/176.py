```python
from typing import List
def remove_duplicates(numbers: List[int]):
    return List(set(numbers))

# Test the function with a sample input
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```
This Python code defines a function called `remove_duplicates` that takes a list of integers as an argument and returns a new list containing only unique elements from the input list, effectively removing duplicates. 

The function uses the set() function to create a set from the input list, and then converts the set back into a list. The resulting output list contains only unique integers from the input list, effectively removing duplicates. 

The code then tests the function by creating a sample list of integers and passing it to the `remove_duplicates` function. The expected output is a list of unique integers, which is printed to the console.