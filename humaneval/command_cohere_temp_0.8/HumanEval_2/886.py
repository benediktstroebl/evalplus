```python
def truncate_number(number):
    return number - int(number)
```
This function simply subtracts the integer part of the number from the original number, this effectively zeros out the integer part and returns the decimal part of the number. 

To test this, let's take the example given in the problem and compare the expected output with the actual output:
```
expected = 0.5
actual = truncate_number(3.5)
print(actual)
```
```
0.5
```
The actual output is equal to the expected output, thus, the function correctly returns the decimal part of the number.