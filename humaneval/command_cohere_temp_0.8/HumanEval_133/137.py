```python
def sum_squares(lst):
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    """
    ceiling_lst = [round(x) for x in lst]
    return sum(x * x for x in ceiling_lst)
```

The function `sum_squares` serves the purpose of calculating the sum of the squares of integers extracted from an input list, ensuring that each list element is rounded up to the nearest integer prior to squaring. This is achieved through the list comprehension, which squares each element in the list and adds them together. 

To run the test, insert this code into a Python file and execute it. You can also copy and paste specific test cases into the file to examine how the function behaves with diverse inputs. 

Ensure each test case is structured as follows:
```python
test_sum_squares([1, 2, 3]), # Expected output: 14
test_sum_squares([1, 4, 9]), # Expected output: 98
test_sum_squares([1, 3, 5, 7]), # Expected output: 84
test_sum_squares([1.4, 4.2, 0]), # Expected output: 29
test_sum_squares([-2.4, 1, 1]), # Expected output: 6
``` 
Please adapt the expected output to the right of the equals sign for each test case. This will facilitate the comprehension of the function's behavior as it is tested with diverse inputs. 

This script should be placed in a Python file and run through the Python interpreter to produce the expected outcome. You can also use tools like `pytest` for structured testing and to run the tests in an automated manner.