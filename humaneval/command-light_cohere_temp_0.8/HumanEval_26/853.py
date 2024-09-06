```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [num for num in numbers if num not in seen and num not in numbers[numbers.repeat[seen]]
seen.
    ```}  See set to keep unique elements only

# Example Test
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # expected output: [1, 3, 4]
``` 
This code uses a set to keep track of the unique elements. The function returns a list of integers, and the set is used to keep track of all elements. The function then returns a list of integers that are not in the set or in the input list.