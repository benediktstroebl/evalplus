```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(0, len(numbers)):
        result.append(numbers[i] + delimeter if i % 2 == 0 else numbers[i])
    return result

# Test cases
test_function = lambda: [1, 2, 3, 4, 5]
test_list = [6,7,8,9,10]

# Function call and assertion
assert intersperse(test_list, 2) == [8, 10, 6, 8, 10, 7] + [9, 5]
```