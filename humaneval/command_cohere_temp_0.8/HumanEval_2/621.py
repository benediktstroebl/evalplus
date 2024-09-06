```python
def truncate_number(number):
    return number - int(number)
```
This function simply subtracts the integer part of the number from the total number, thus returning just the decimal part. 

To test this script, you can call the function with a float input like so: 
 ```python
truncate_number(3.5)
```
The output will be: 
 ```
0.5
``` 
This is the decimal portion of the figure that was trimmed off.