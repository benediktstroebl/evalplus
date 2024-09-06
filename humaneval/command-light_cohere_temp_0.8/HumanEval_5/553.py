```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(len(numbers)):
        if i % 2 == 0:
            result.append(numbers[i] + delimeter)
        else:
            result.append(numbers[i])
    return result

# Test the function
numbers = [1, 2,3,4,3,2,1]
result = intersperse(numbers, 2)
print(result)  # Output: [1,2,3,2,3,4,3,2,1]
```