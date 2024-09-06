```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        result.append(delimiter)
        result.append(num)
    return result

# Test the function with the same inputs
numbers = [1, 2, 3]
delimiter = 4
expected = [1, 4, 2, 4, 3]
result = intersperse(numbers, delimiter)
assert list(result) == expected
 ```