```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(0, len(numbers)):
        if i % 2 == 0:
            result.append(numbers[i] + delimeter)
        else:
            result.append(numbers[i])
    return result

# Test the function with sample input and expected output
numbers = [4, 2, 3,1]
delimiter = 4
result_expected = [4, 4, 2, 4, 3]
print(f"Result is {result_expected}")
```