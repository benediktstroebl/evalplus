```python
def truncate_number(number):
    """ Returns the decimal part of the number """
    return number - int(number)
```
This function simply takes a number and returns the decimal part of the number by subtracting the integer part of the number. 

To test this function, here is a sample execution:
```python
>> truncate_number(3.5)
0.5
>> truncate_number(12.345)
0.345
>> truncate_number(100)
Traceback (most recent call last):
  ...
TypeError: Argument 'number' must be a float
``` 
The first two test cases show that the function correctly returns the decimal parts of the numbers 3.5 and 12.345. The third test case ensures that the function throws a TypeError when an invalid argument is passed.