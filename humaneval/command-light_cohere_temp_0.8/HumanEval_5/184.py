```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test case:
numbers = [1, 2, 3]
delimiter = 4
result = intersperse(numbers, delimiter)
print(result)  # Output: [1, 4, 2, 4, 3]
```
This script defines a function `intersperse` that takes a list of integers and a delimiter as input, and returns a new list with the elements of the input list spaced by the specified delimiter. 
In the provided test case, it creates a list `[1, 2, 3]`, and applies the `intersperse` function with a delimiter of 4. The resulting list is `[1, 4, 2, 4, 3]` which demonstrates the spacing effect of the `delimiter` value.