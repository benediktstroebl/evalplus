```python
def add(x: int, y: int):
    return x + y
```
The function takes in two arguments, x and y, both of type `int`. It returns the result of adding the two numbers together. 

To pass tests, consider adding the following lines to your script:
```python
>>> print(add(2, 3))
5
>>> print(add(5, 7))
12
```
These lines of code call the `add` function with different arguments and print the expected output for each test case. Make sure to adjust the printed values in accordance with your expected output. 
The doc strings describe the behavior of the function and also reflect the corresponding test cases, which are designed to confirm that the function behaves as expected. GIVEN THIS SETUP, THE FUNCTION SHOULD SUCCESSFULLY PASS BOTH TEST CASES.