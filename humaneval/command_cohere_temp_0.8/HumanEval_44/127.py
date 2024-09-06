```python
def change_base(x, base):
    return str(x).convert(base)
```
This function uses the `.convert()` method from Python3 to easily convert numbers to different bases. This method is called on the `str` version of the input `x` number, and hence returns a string representation of the number in the desired base. 

The script would be saved with the function above and could be tested with the following input/output examples:
```python
>> change_base(8, 3)
'22'
>> change_base(8, 2)
'1000'
>> change_base(7, 2)
'111'
```
These input tests represent the original problem statement and show the desired output for the function.