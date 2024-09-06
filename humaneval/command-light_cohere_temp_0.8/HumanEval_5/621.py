```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list.
    Args:
        numbers (List[int]): List of integers.
    Returns: List[int].
    """
    result = [num] + [delimiter] + [num + delimiter] + [delimiter] + [num] + [delimiter] + [num + delimiter]
    while len(numbers) > 1:
        numbers[0], numbers[1] = numbers[1], numbers[0]
    return numbers

# Test case
numbers = [1, 2, 3, 4, 10, 2]
result = intersperse(numbers, 4)
print(result)  # Output: [1, 4, 2, 10, 3, 4, 2, 10, 1, 4, 3]
```