```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(0, len(numbers)):
        if i % 2 == 0:
            result.append(numbers[i] + delimeter)
        else:
            result.append(numbers[i])
    return result

# Tests
numbers = [1, 2,3,4,3,2,1]
result = disperse(numbers, 2)
print(result)  # Output: [1,2,3,4,3,2,1]
```