```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of the input list.
    :param numbers: List[int], int
    :param delimeter: int
    :return: List[int]
    """
    numbers = [num for num in numbers if num != delimeter] + [delimeter] + [num for num in numbers if num != delimeter]
    return numbers

# Test Case 1:
test_case1 = [4, 2, 3]
test_case1_res = intersperse(test_case1, 2)
assert list(test_case1_res)==[ [4, 2, 2, 3] )

# Test Case 2:
test_case2 = [1, 2, 3, 4]
test_case2_res = intersperse(test_case2, 2)
assert list(test_case2_res)== [1, 2, 4, 4, 3] 
``` 
This Python function, **'intersperse'**, accepts a list of integers and a delimiter as inputs. The function first adds a numbers that are not equal to the delimiter to the output list, then adds the delimiter, and finally, adds the numbers that are not equal to the delimiter.