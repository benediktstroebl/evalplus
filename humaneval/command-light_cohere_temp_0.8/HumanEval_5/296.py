```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(len(numbers) - 1):
        result.append(numbers[i] + delimeter)
    result.append(numbers[i])
    return result

# Test case 1: Basic function usage
numbers = [1, 2, 3]
result = intersperse(numbers, 4)
print(result)

# Test case 2: Passing custom list with different lengths
numbers_list = [1, 2, 3, 4, 5]
result = intersperse(numbers_list, 4)
print(result)

# Test case 3: Passing empty list
numbers_empty = []
result = intersperse(numbers_empty, 4)
print(result)
```
This Python script defines a function `intersperse` that takes a list of numbers and a delimiter as input and returns a new list with the numbers separated by that delimiter. The script then provides three test cases to demonstrate the function's behavior: passing a basic list, a list with different lengths, and an empty list.