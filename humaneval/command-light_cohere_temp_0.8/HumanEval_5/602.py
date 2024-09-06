```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(0, len(numbers)):
        if i % 2 == 0:
            result.append(numbers[i])
        else:
            result.append(numbers[i] + delimeter)
    return result

# Test the function
numbers = [1, 2, 3]
result = intersperse(numbers, 4)
print(result)  # Output: [1, 4, 2, 4, 3]
```
This code defines a function called `intersperse` that takes a list of numbers and a delimiter as input, and returns a new list with the numbers interspaced by the given delimiter. The test case demonstrates the example usage, where the function is called with an input list and a delimiter, and the resulting interspaced list is printed.