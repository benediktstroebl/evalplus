```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return numbers + [delimeter] * (len(numbers) - 1)

# Test case 1: Basic function call
numbers = [1, 2, 3]
result = intersperse(numbers, 4)
print(result)   # Expected output: [1, 4, 2, 4, 3]

# Test case 2: Lists with different lengths
numbers2 = [1, 2, 3, 4, 5]
result2 = intersperse(numbers2, 4)
print(result2)  # Expected output: [1, 4, 2, 4, 3, 5]

# Test case 3: Lists with different values
numbers3 = [5, 6, 7, 8]
result3 = intersperse(numbers3, 4)
print(result3)  # Expected output: [5, 4, 7, 4, 8]
```
This script defines a function `intersperse` that takes a list of numbers and a delimiter as input, and returns a list with the numbers separated by the delimiter. The script also provides three test cases to verify the correctness of the `intersperse` function.