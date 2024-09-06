```python
def sort_numbers(input_string: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    """
    numbers = input_string.split()
    numbers.sort()
    return ' '.join(numbers)
```
The function takes a string as input and returns a string with the numbers sorted in ascending order. 
The function first splits the input string into a list of numbers, then sorts that list, and finally joins the sorted list of numbers back into a string for the output.

Here is a sample test case that could be used to test this function:
```python
test_case = 'one five three'
expected_result = 'one three five'
result = sort_numbers(test_case)
assert result == expected_result
``` 

This test case checks if the output of the `sort_numbers` function is as expected when given the input `one five three`. 
It verifies that the numbers 'one', 'three', and 'five' are sorted in that order and then joined into a single string. 
The `assert` statement will throw an error if the test case fails, adding further information to the assertion in order to distinguish why the test case failed.