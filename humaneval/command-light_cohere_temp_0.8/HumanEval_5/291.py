```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(0, len(numbers)):
        if i % 2 == 0:
            result.append(numbers[i] + delimeter)
        else:
            result.append(numbers[i])
    return result

# Unit tests
test_ints = [4, 2,3]
test_result = intersperse(test_ints, 2)
print(test_result)

test_lists = [[1,2,3], [4,5,6],[7,8,9]]
test_result = intersperse(test_lists, 4)
print(test_result)

test_strings = ["Python", "JavaScript","C++"]
test_result = intersperse(test_strings, ' ')
print(test_result)
```