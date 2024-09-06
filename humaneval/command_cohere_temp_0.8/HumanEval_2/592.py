```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than the input number from the input number, which inherently truncates the decimal part and returns it on its own. 

To test this script, you can call the function with any floating point number and the result will be the decimal part of that number. For example:
```python
 truncate_number(3.5)
```
This will print "0.5", which is the decimal part of the number 3.5. 
If you wish to test this function with a more extensive set of floating-point inputs, feel free to do so and examine the results, as the function should consistently return the decimal part of any input it receives.