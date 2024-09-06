```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i+delimiter for i,j in zip(numbers,numbers[1:]+[delimeter])]
# Example test case:
if __name__ == "__main__":
    numbers = [1, 2, 3]
    delimiters = [4, 4, 2, 4, 3]
    print(inperse(numbers, delimiters))
```
In this code, we've encapsulated a function called `intersperse` that takes two arguments: a list of integers `numbers` and an integer `delimiter`. The function uses a list comprehension to iterate through pairs of adjacent elements in the `numbers` list, and adds the `delimiter` between each pair. This creates a result in a list of numbers with the `delimiter` inserted between every two consecutive elements. The example provided in the code will print the `numbers` list with the `delimiters` added.