```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   
    return result

# Example usage
numbers = [1, 2, 3, 2, 4,3,1]
print(remove_duplicates(numbers))
``` 
This code defines a function **`remove_duplicates`** that removes duplicate values from a list. The function utilizes a set to keep track of seen elements and creates a new list with all distinct values from the input list. 

The output of the code will be **`[1, 2, 3, 4]`**, which are the distinct elements from the input list.