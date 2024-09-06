```python
def truncate_number(number):
    return number - int(number)
```

The function takes in a `number` as an input and returns the decimal part of the number. This is accomplished by taking the difference between the number and the greatest integer value that is less than or equal to the number, which is achieved using the `int()` function. The resulting difference is the desired decimal part of the number. 

To test this function, you can call it with a variety of numerical inputs and compare the result to the expected output. 

For example:
```python
truncate_number(3.5) == 0.5
```
Should return `True` since the output of the function, in this case, is `0.5`, and this is the expected output for the input of `3.5`. 

This function should handle all positive floating point numbers, since the `int()` function correctly rounds the number down to the nearest integer. 

Let me know if you'd like me to cover more examples or provide further clarification on the solution!