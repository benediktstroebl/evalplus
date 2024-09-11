### Interspersing Numbers in a List
```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): The input list of integers.
        delimeter (int): The number to be inserted between each pair of consecutive elements.

    Returns:
        List[int]: The modified list with 'delimeter' inserted between each pair of consecutive elements.
    """
    if not numbers:  # Base case: If the list is empty, return it as is.
        return numbers
    
    result = [numbers[0]]  # Start the result list with the first element of the input list.
    
    for num in numbers[1:]:  # Iterate over the rest of the input list.
        result.append(delimeter)  # Insert the delimeter before each element.
        result.append(num)
    
    return result

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```
This script defines a function `intersperse` that takes two parameters: `numbers`, a list of integers, and `delimeter`, an integer to be inserted between each pair of consecutive elements. The function returns a new list with the `delimeter` inserted between each pair of consecutive elements. The script also includes two test cases to demonstrate the function's behavior.