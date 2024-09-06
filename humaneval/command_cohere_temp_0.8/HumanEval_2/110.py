```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply subtracts the integer part of the number from the original number, leaving behind the decimal part. 

To test this function, you can call it with a float input like so: 
```python
input_number = 3.5
truncated = truncate_number(input_number)
print(f"The truncated part of {input_number} is: {truncated}")
```
This should print:
```
The truncated part of 3.5 is: 0.5
``` 

This confirms that the function correctly returns the decimal part of the input number. 

I hope this solves your problem! Let me know if you have any more questions.