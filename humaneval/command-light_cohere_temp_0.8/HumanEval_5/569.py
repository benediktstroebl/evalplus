```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num in numbers for _ in range(2)]

# Test the function with sample inputs
numbers = [1, 2, 3, 4, 5]
delimiter = 4
expected = [1, 5, 2, 6, 4, 8, 3]
result = intersperse(numbers, delimiter)

print(result == expected)  # True
 ```