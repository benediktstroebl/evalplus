```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Args:
        numbers (List[int]): Input list of integers
        delimeter (int): Number to be inserted between the elements

    Returns:
        List[int]: Modified list with the delimeter inserted
    """
    if not numbers:  # If the input list is empty, return it as is
        return numbers
    
    result = [numbers[0]]  # Start with the first element of the input list
    for num in numbers[1:]:  # Iterate over the rest of the list
        result.append(delimeter)  # Insert the delimeter before each number
        result.append(num)
    
    return result[:-1]  # Remove the extra delimeter at the end

# Example usage
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script uses a simple iterative approach to solve the problem. It starts by checking if the input list is empty, in which case it returns the list as is. Then, it creates a new list with the first element of the input list. It then iterates over the rest of the list, inserting the delimeter before each number. Finally, it returns the modified list, excluding the extra delimeter at the end.