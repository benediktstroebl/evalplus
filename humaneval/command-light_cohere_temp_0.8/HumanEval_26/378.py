```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in numbers[numbers.count()]]
List(numbers)  # Pass-through for testing
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Expected output: [1, 3, 4]
``` 
This Python code defines a function called `remove_duplicates`, designed to take a list of integers as input and generate a new list with integers that have not duplicates. The function utilizes a unique element identification through a generator expression with the `count()` function to filter out any duplicate elements from the input list.