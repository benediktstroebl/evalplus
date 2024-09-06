```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [num for num in numbers if num not in seen and num not in numbers[numbers.index]]

numbers = [1, 2, 3, 2, 4, 3, 5]
result = remove_duplicates(numbers)
print(result)
``` 
This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with all integers that have not been duplicates. The script then creates an list of numbers, passes it to the function, and prints the result, which should be `[1, 3, 4]`, because these are the unique integers.