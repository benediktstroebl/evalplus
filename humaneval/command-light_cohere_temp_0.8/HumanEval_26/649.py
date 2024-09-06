```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return [result])
    return result

test_remove_duplicates = [1, 2, 3, 2, 4]
result = remove_duplicates(test_remove_duplicates)
print(result)  # Output should be: [1, 3, 4]
``` 
This function removes duplicate elements from the input list and returns the modified list.  It can be used to pass various tests to ensure the functionality of the function.