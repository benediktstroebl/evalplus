```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list `numbers' """
    
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over the input list with enumerate to have access to index and value
    for i, num in enumerate(numbers):
        # Append the current number to the result list
        result.append(num)
        
        # If it's not the last element in the list, append the delimiter
        if i < len(numbers) - 1:
            result.append(delimiter)
    
    return result

# Test cases
print(intersperse([], 4))  # Expected output: []
print(intersperse([1, 2, 3], 4))  # Expected output: [1, 4, 2, 4, 3]
```

Alternatively, you can use a more Pythonic way to solve this problem using list comprehension and the `itertools.chain` function:

```python
from typing import List
import itertools

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list `numbers' """
    
    # Use itertools.chain to flatten the list of lists into a single list
    return list(itertools.chain(*[[num, delimiter] if i < len(numbers) - 1 else [num] for i, num in enumerate(numbers)]))

# Test cases
print(intersperse([], 4))  # Expected output: []
print(intersperse([1, 2, 3], 4))  # Expected output: [1, 4, 2, 4, 3]
```

Or, you can use the `reduce` function from the `functools` module:

```python
from typing import List
import functools

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list `numbers' """
    
    # Use functools.reduce to concatenate the lists
    return functools.reduce(lambda x, y: x + [delimiter, y] if x else [y], numbers, [])

# Test cases
print(intersperse([], 4))  # Expected output: []
print(intersperse([1, 2, 3], 4))  # Expected output: [1, 4, 2, 4, 3]
```