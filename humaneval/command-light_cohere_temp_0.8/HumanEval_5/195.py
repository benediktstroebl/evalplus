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
test_strs = ['a', 'b', 'c']
test_lists = [['item1', 'item2', 'item3'], ['item1', 'item2', 'item3','item4'], [1,2,3] ]

for test in test_ints:
    assert intersperse(test, 2) == [4, 2, 3, 4]

for test in test_strs:
    assert intersperse(test, 3) == ['a', 'b', 'c']

for test in test_lists:
    assert intersperse(test, 2) == [1, 2, 3, 4]

print('All tests passed!')
```  This script defines a function **'intersperse'** that takes in a list of integers and a delimiter as input and returns a list of integers with the delimiter inserted between every other element in the list. The script then creates several test cases to check the correctness of the function by comparing the output with the expected results.