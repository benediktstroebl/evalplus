```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [num for num in numbers if num not in seen and num not in numbers[numbers.keys() &set_ duplicates(seen) ]

numbers = [1, 2, 3, 2, 4, 3, 1, 4]
print(remove_duplicates(numbers))
``` 
This code defines a function called `remove_duplicates` that takes a list of integers as an argument. It creates a `seen` set that stores unique elements from the input list. It then iterates through elements in the input list and checks if the number is already in the `seen` set or in the original input list. If the number is not seen before or is not in the input list, it adds it to the `seen` set. Finally, the list of numbers that were not seen before and are not in the input list are returned.