```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]
# Example usage:
numbers = [1, 2, 3]
delimiter = 4
result = intersperse(numbers, delimiter)
print(result)
``` 
This code defines a function `intersperse` that takes a list of integers `numbers` and an integer `delimiter` as input. The function uses a formula to add the `delimiter` between every two consecutive elements in the list, resulting in the desired effect of inserting the `delimiter` between numbers. 
The example provided shows how to use the function with a sample list and print the resulting list.