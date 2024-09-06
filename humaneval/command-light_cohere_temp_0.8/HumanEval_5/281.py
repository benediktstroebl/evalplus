```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list.
    :param numbers: list of integers
    :param delimiter: positive integer
    :return: list of integers with spacing
    """
    return [num + delimiter if num != 0 else num for num in numbers]

# Test case 1
test_case_1 = [4, 2, 3]
test_result_1 = intersperse(test_case_1, 4)
print(test_result_1)

# Test case 2
test_case_2 = [1, 2, 3, 4]
test_result_2 = intersperse(test_case_2, 4)
print(test_result_2)

# Test case 3
test_case_3 = [3, 2, 1]
test_result_3 = intersperse(test_case_3, 4)
print(test_result_3)
```