### Interspersing a List of Numbers with a Given Delimeter

Below is a Python script that defines a function `intersperse` to insert a given delimeter between every two consecutive elements of a list of numbers.

```markdown
### Code

```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    
    Args:
    numbers (List[int]): List of integers
    delimeter (int): Number to be inserted between list elements
    
    Returns:
    List[int]: List with delimeter inserted between list elements
    """
    result = [numbers[0]]  # Start with the first element
    
    for num in numbers[1:]:  # Iterate over the rest of the list
        result.extend([delimeter, num])
    
    return result

# Test cases
print(intersperse([], 4))  # Expected output: []
print(intersperse([1, 2, 3], 4))  # Expected output: [1, 4, 2, 4, 3]
print(intersperse([5], 6))  # Expected output: [5]
print(intersperse([1, 2, 3, 4, 5], 0))  # Expected output: [1, 0, 2, 0, 3, 0, 4, 0, 5]
```

### Explanation

This script defines a function `intersperse` that takes two parameters: a list of integers `numbers` and an integer `delimeter`. It returns a new list with the `delimeter` inserted between every two consecutive elements of the `numbers` list.

The function starts by initializing a new list `result` with the first element of the `numbers` list. It then iterates over the remaining elements of the `numbers` list, appending the `delimeter` followed by the current element to the `result` list.

Finally, the script includes test cases to demonstrate the function's behavior with different inputs.