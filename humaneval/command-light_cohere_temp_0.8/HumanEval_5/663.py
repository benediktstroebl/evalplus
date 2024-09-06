```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter if i < len(numbers) - 1 else num for i, num in enumerate(numbers)]

# Unit tests
numbers = [1, 2, 3, 4]
delimiters = [0, 0, 0, 0]
result = intersperse(numbers, delimiters)
shouldBe = [1, 3, 2, 4, 3]

assert list(result) == shouldBe
print(result == shouldBe)  # This will print True
```