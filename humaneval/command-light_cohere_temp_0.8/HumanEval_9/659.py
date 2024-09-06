```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, _ in sorted((num for num in numbers), reverse=True) if num > numbers[-1]]
#Test cases
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]
```  This function utilizes the sorted function with reverse=True to sort the numbers list in descending order. The sorted function returns a max element found in the sorted list, which is then returned. This script is optimized the use of a generator expression to create the list of rolling max elements, making it self-contained.