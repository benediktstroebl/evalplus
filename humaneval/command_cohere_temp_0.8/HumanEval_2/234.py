```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply converts the float `number` to an integer using `int()`, and then returns the difference between the original number and the integer, which results in the decimal part of the original number. 

To test this function, you can call it with a float input, and compare the returned value with the expected output. 
For example: 
 ```python
from truncate_number import truncate_number

test_result = truncate_number(3.5)
print(test_result)  # Expected output: 0.5
``` 
The output should correspond to the example provided in the problem statement.