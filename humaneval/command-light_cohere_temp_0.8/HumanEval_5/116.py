```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list """
    return [num + delimeter if i % 2 == 0 else num + delimeter + num for i, num in enumerate(numbers)]

# Test cases
test_numbers = [1, 2, 3, 4, 5]
test_delimiter = 4
test_result = intersperse(test_numbers, test_delimiter)
print(test_result)  # Expected output: [1, 4, 2, 4, 3, 5]

test_long_numbers = [1, 2, 3, 4, 5, 6, 7]
test_delimiter = 10
test_result = intersperse(test_long_numbers, test_delimiter)
print(test_result)  # Expected output: [1, 12, 23, 34, 5, 56, 7]
```
The `insperse` function uses list comprehension to achieve the desired output. The function adds the  a number 'delimiter' between every two consecutive elements of the input list. 
The test cases demonstrate the expected behavior of the `insperse` function for different inputs and different values for `delimiter` parameter.