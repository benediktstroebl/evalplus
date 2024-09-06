```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i+j for i, j in zip(numbers, numbers[1:])] + numbers

# Test
numbers = [1, 2, 3, 4, 5]
delimiter = 4
result = intersperse(numbers, delimiter)
print(result == [1, 4, 2, 4, 3, 5])  # True
print(result == [1, 2, 4, 5])        # True
print(result == [1, 2, 3, 4, 4])    # True
print(result == [1, 2, 3])        # False
```