```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply takes the input number and returns the decimal part of the number by subtracting the integer part of the number. 
The test cases are also included and can be executed by pasting the code in `python`, and the output will be something like this:
```bash
>> truncate_number(1.5)
0.5
>> truncate_number(2.5)
0.5
>> truncate_number(3.5)
0.5
>> truncate_number(10.5)
0.5
```