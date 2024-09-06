```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply takes the input number and returns the decimal part of the number by subtracting the integer part of the number. 
The test case will be an example of the function usage:
```python
truncate_number(3.5)  # Should return 0.5
``` 
This test case will verify if the output of the function when the number 3.5 is passed as an input is 0.5. 
Please note that no actual decimal part will be cut or truncated from the number, this function simply gives you back the decimal part of the number, in case you need it for any other calculations. 
Let me know if anything needs further clarification or if you want to go through more examples of function usage and refinement. 
You can also copy and paste the above code into a Python file (e.g., `truncate_number.py`) and run the tests using the `pytest` command ('python -m pytest truncate_number.py') to validate the functionality.