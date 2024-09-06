Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This script defines a function called `incr_list` that takes a list argument and returns a new list with its elements incremented by 1. It uses a list comprehension to iterate over each element in the input list and calculates the incremented value by adding 1 to each element. 

To confirm the functionality of the solution, you can add test cases in the same file using the `pytest` framework and then execute the tests using the command `pytest TEST_FILE.py`. Here's an example:
```python
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
``` 
This will verify the correctness of the solution and provide confidence that it behaves according to the specified problem statement. 
Here is the complete Python script:
```python
# The following code is a complete Python script that demonstrates the use of the incr_list function
# It includes test cases using the pytest framework

def incr_list(l: list):
    result = [x + 1 for x in l]
    return result

def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]

# To execute the test, run the following command from the command line
# pytest TEST_FILE.py
``` 
Note that the function `incr_list` is defined with a list parameter `l` and a return value of type list. The function uses a list comprehension to iterate over the list and return a new list with the elements incremented by 1. 

This code can be imported and used as a module in other Python scripts that need a function to increment the elements of a list by 1. For further clarity on the intended use of the function and the expected behavior of the code, documentation may be added, including descriptions of the function, parameters and return values as well explanations of the test cases.  This helps users better understand the purpose of this code and how to effectively use the `incr_list` function in their applications.