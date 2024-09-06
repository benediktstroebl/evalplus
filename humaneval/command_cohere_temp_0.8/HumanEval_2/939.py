```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply takes a number, subtracts the closest integer to it (using int() to truncate), and returns the result, which is the decimal part of the number. 

To test this function, you can call it with a few sample numbers and compare the result to the expected output. 
For example:
```python
truncate_number(3.5) == 0.5
truncate_number(12.345) == 0.345
truncate_number(101.3) == 0.3
```
The function should return True for each assertion, indicating that it produces the expected output.  This approach is concise and straightforward, making it easy to understand and maintain.