Here's a Python script with a self-contained function that solves the problem:
```python
def get_positive(l):
    return [x for x in l if x > 0]
```
This function uses a list comprehension, which is a short way of writing a for loop, to create a new list `x` that only includes elements `x` from the input list `l` that are greater than zero, disregarding any other elements present in `l`. 

The function outputs a list of all the positive numbers in the input list. 

To verify the functionality of the script, you can use the following test cases to test the behavior of the function on a variety of inputs: 
```python
>> get_positive([-1, 2, -4, 5, 6])
[2, 5, 6]
>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
[5, 3, 2, 3, 9, 123, 1]
>> get_positive([0, -1, 2, 3, -4, 5, -6, 7, 8, -9, 10])
[2, 3, 5, 7, 8, 10]
>> get_positive([-11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
Each of these test cases demonstrates how the `get_positive()` function can be used to filter a list of numbers to include only the positive numbers. 

The expected output for each test case is included within the comment `>>` on the same line as the function call. 
The resulting output is then displayed as a new line following the test case. If the output matches the expected output, this indicates that the function is working as intended, as these varied inputs and expected outputs have been validated.