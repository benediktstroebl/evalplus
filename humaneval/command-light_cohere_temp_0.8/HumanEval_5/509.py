```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return numbers[:-delimiter] + [number] + numbers[-1:]delimiter

# Test cases with a variety of inputs
numbers = [10, 100, 2, 3, 20]
delimiter = 3

expected = [10, 13, 15, 17, 20]
result = intersperse(numbers, delimiter)

print(result == expected)  # Should print True
```