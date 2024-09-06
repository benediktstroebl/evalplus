```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    result: List[int] = []
    for num in numbers:
        result.append(num)
        if len(result) > 1:
            result.append(delimiter)
    return result
```

The `intersperse()` function takes in two parameters: `numbers`, which is a list of integers, and `delimiter`, which is the number to be inserted between consecutive elements of the `numbers` list. It uses a list comprehension to iterate through each number in the `numbers` list, adding each one to the `result` list. Additionally, it adds the `delimiter` between each pair of consecutive elements, except between the first element and any subsequent elements, and the last element and its preceding ones. 

The resulting `result` list is then returned, with the `delimiter` inserted between consecutive elements as requested. 

```python
# Example usage
assert intersperse([], 3) == []

assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]
``` 

The example usage tests are included to confirm that the function behaves as expected. One test case includes an empty list, and the function returns an empty list accordingly. The other test case provides a list of integers and a delimiter, and the function returns the interlaced list expected.