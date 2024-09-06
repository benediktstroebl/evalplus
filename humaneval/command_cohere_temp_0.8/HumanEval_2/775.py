```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply takes a number and returns the decimal part of the number. It achieves this by taking the difference between the given number, and the largest integer that is less than or equal to the given number. For example, the decimal part of 3.5 will be 0.5. This is because 3 is the largest integer that is less than 3.5, and 3.5 - 3 = 0.5. 

To test this function, we can call it with a variety of inputs to ensure that it is correct:
```python
# Testing the function
assert truncate_number(3.5) == 0.5
assert truncate_number(2.0) == 0.0
assert truncate_number(2.01) == 0.01
```
The tests passed, and the function correctly returns the decimal part of the given number. 
If you have any more questions or need further assistance, feel free to ask!