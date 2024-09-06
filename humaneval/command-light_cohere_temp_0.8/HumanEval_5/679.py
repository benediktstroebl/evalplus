```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test case:
numbers = [1, 2, 3]
delimiters = [4, 8]
result = intersperse(numbers, delimiters)
print(result)

# Test case 2:
numbers = [1, 2, 3, 4, 5]
delimiters = [2, 4]
result = intersperse(numbers, delimiters)
print(result)
```
The function `intersperse` takes a list of numbers and an integer `delimiter` as input and returns a new list with the numbers separated by that `delimiter`. The function uses a list comprehension and the `enumerize` function to iterate over the input list and add the `delimiter` between every two consecutive elements. 
Test cases have been provided to demonstrate the function.