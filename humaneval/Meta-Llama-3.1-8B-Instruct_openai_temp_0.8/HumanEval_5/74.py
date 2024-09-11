### Interspersing Numbers in a List

Below is a Python function that takes a list of integers and an integer as input and returns a new list with the integer delimeter inserted between every two consecutive elements of the input list.

```markdown
### Code

```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    
    Args:
        numbers (List[int]): A list of integer values
        delimeter (int): The number to be inserted between consecutive elements
        
    Returns:
        List[int]: The modified list with delimeter inserted between consecutive elements
    """
    if not numbers:  # if the list is empty, return an empty list
        return []
    
    result = [numbers[0]]  # start with the first element of the list
    
    for num in numbers[1:]:  # iterate over the rest of the list
        result.append(delimeter)  # insert delimeter before each element
        result.append(num)  # append the current element
    
    return result

### Test Cases

print(intersperse([], 4))  # expected output: []
print(intersperse([1, 2, 3], 4))  # expected output: [1, 4, 2, 4, 3]
print(intersperse([1, 2, 3, 4, 5], 0))  # expected output: [1, 0, 2, 0, 3, 0, 4, 0, 5]
```

### Explanation

The `intersperse` function takes a list of integers and an integer as input and returns a new list. It starts by checking if the input list is empty. If it is, the function returns an empty list.

If the list is not empty, the function starts with the first element of the list in the result list. It then iterates over the rest of the list, inserting the delimeter before each element and appending the current element to the result list.

Finally, the function returns the modified list with the delimeter inserted between consecutive elements.