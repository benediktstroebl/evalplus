```python
def number_of_odd_digits(string_list):
    result = ['the number of odd elements in the string %s of the input.' % i for i in range(len(string_list))]
    [result[i] = str(string_list[i].count('1')) for i in range(len(string_list))]
    return result
```

This code defines a function called `number_of_odd_digits` which takes a list of strings as input. It then returns a list where each element is described by the number of odd digits in the i'th string in the input list. The function uses a list comprehension which creates a new list from the descriptions, then replaces the i'th element with the number of '1's in the i'th string in the input list. The result is a list of modified descriptions, each indicating the count of odd digits in the corresponding string. 

To ensure the functionality, here are some tests to check the correctness of the provided solution:
```python
def test_odd_count():
    # Test list of strings with only digits
    assert odd_count(['1234567']) == ["the number of odd elements in the string 4 of the input."]

    # Test list of strings with only odd digits
    assert odd_count(['3', "11111111"]) == ["the number of odd elements in the string 1 of the input.", "the number of odd elements in the string 8 of the input."]

    # Test list of strings with mixed digits
    assert odd_count(['13579', '123', '111']) == ["2", "1", "4"]

    # Test list of strings with no odd digits
    assert odd_count(['34567', '22345', '12345']) == ["0", "0", "0"]

test_odd_count()
```

These tests aim to validate the behavior of the function for different scenarios, including lists containing exclusively odd or even digits, a mix of both, and cases with no odd digits. 

The function is then executed with test_odd_count() to check if the function works as expected. 
If you don't have Python installed on your device, you would need to install it in order to run the test file.