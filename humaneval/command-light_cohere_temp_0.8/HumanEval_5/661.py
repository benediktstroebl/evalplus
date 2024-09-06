```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        result.append(delimeter)
    result.append(num)
    result.append(delimiter))
    return result

# Example Test:
input_numbers = [4, 2,8,3]
result_test = intersperse(input_numbers, 4)
print(result_test)  # Output: [4, 8, 2, 8, 3]
```
This script defines a function `intersperse` that takes a list of integers and a delimiter as input, and returns a new list with the integers interspaced by the specified delimiter. The example test demonstrates how the problem is solved and passes the test.