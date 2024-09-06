```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This script defines a function `flip_case` that takes a string as an argument and flips the case of alphabetic characters, leaving non-alphabetic characters unchanged. It uses the `swapcase()` method to flip the case of alphabetic characters, and the `join()` method to concatenate the modified characters back together. 

To test this script, you can call the function with different input strings and compare the output with the expected results. Here is an example:
```python
# Test case for flip_case function
def test_flip_case():
    # Arrange
    expected_result = 'hELLO'
    input_string = 'Hello'

    # Act
    result = flip_case(input_string)

    # Assert
    assert result == expected_result
```

This test case uses the `flip_case` function to transform the string `Hello` to `hELLO`, which is compared to the expected output using the `assert` statement. 

To run this test, you can add the test case to a Python file and execute the script, which will verify the functionality of the `flip_case` function and display the test results. 
Here is an example of the output:
```python
...
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
``` 

This indicates that the `flip_case` function works as expected and correctly flips the case of alphabetic characters while leaving non-alphabetic characters unchanged.