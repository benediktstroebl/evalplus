```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [num for num in numbers if num not in seen and num not in numbers[seen]]


# Example usage and tests
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print("Result:", result)
print("Input elements:", numbers)
print("Output elements:", result)

numbers = [1, 2, 3, 3, 4]
result2 = remove_duplicates(numbers)
print("Result2:", result2)

numbers = [1, 2, 3, 4, 5, 6]
result3 = remove_duplicates(numbers)
print("Result3:", result3)
``` 
This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicates removed. The function uses a set to keep track of elements seen before and then uses list comprehension to filter out elements that are not in the set and also not in the input numbers list. The example usage demonstrates the example of passing the function multiple times with different inputs, and it prints the results for each case.