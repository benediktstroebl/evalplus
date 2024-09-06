```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    result = []
    seen = set()
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return theresult
numbers=[1, 2, 3, 2, 4, 1, 3,4]
result = remove_duplicates(numbers)
print(result)
``` 
This function uses a set to keep track of seen numbers, and then appends any number not in the set to the result list. The function can be easily used to solve the problem and pass corresponding tests.