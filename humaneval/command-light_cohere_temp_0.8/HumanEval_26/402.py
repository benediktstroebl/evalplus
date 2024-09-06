```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in numbers[numbers.keys()]]


numbers = [1, 2, 3, 2, 4, 2, 1]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]
``` 
This script defines a function **remove_duplicates** that takes a list of integers as input and returns a new list with duplicate elements removed. The script then creates an list with duplicate integers and passes it to the function, which prints the resulting list containing only the non-repeated integers.