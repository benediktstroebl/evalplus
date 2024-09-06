```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply subtracts the integer part of the number from the original number, effectively leaving only the decimal part. 

To test this function, you can call it with a float input like so: 
```python
input_number = 3.74
truncated = truncate_number(input_number)
print(f"The truncated value of {input_number} is: {truncated}")
```
This should print:
```
The truncated value of 3.74 is: 0.74
``` 

This demonstrates that the function correctly isolates the decimal portion of the original number. 

Let me know if you need any further refinements to this code!