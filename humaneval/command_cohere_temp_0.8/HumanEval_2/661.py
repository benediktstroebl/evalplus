```python
def truncate_number(number):
    return number - int(number)
```
This function simply subtracts the largest integer less than or equal to `number` from `number` which yields the original number minus its integer part, which is the requested decimal part of the number. 

Here is a simple test case to confirm the functionality of the function:
```python
 truncate_number(3.5)
# Expected output: 0.5
``` 
and the code will output: 
 ```python
0.5
``` 

Please note that the assumption here is that the number is a positive floating point number, and the integer part is the largest integer less than or equal to the number, which is the standard definition of the floor function in mathematics. 

If the number can be negative or the definition of the integer part needs to be changed, the original problem statement needs to be adjusted accordingly.