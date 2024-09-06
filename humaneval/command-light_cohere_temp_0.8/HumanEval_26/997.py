```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return thereturn: result

# Test
input_list = [1, 2, 3, 2, 4]
result_test = remove_duplicates(input_list)
print(result_test)  # Output: [1, 3, 4]

``` 
This script defines a function `remove_duplicates` that takes a list of integers and returns a new list with duplicate values removed. It uses a technique of using a set to keep track of seen values, and then adds elements to the result list if they are not duplicates.