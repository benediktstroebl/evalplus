```python
def truncate_number(number):
    return number - int(number)
```
This Python script defines a function called truncate_number, which takes a single argument number. This function returns the decimal part of the input number. It does so by subtracting the integer part of the number (obtained by converting it to an integer) from the original number. 

For example, if the variable `number` is set to `3.5`, the function truncate_number(3.5) returns `0.5`, as described in the markdown code block. 

This solution leverages Python's implicit casting within arithmetic operations, providing a concise way to isolate the decimal part of a floating-point number. 
It does not require any additional libraries or dependencies.