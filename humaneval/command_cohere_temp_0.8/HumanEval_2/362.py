```python
def truncate_number(number):
    return number - int(number)
```
This Python script defines a function called `truncate_number` that takes in a single argument, `number`, which is expected to be a positive floating point number. Inside the function, the `int` function is used to convert the input number to an integer, which effectively discards the decimal part of the number. The result is the difference between the original number and the integer part. This difference is returned as the decimal part of the original number. 

Therefore, if you input `3.5` into the function, the result will be `0.5`, which is the decimal part of `3.5`. 

The script assumes that the input number is valid, excluding negative numbers or whole numbers (those that do not have a decimal part). It caters to the specified requirement of returning the decimal part of the number, making it useful for specific scenarios where decimal handling is needed. 

If you need to check if the input is a valid floating point number, you can introduce a validation step before applying the truncation logic. Here is an example: 
```python
def truncate_number(number):
    if not isinstance(number, float) or int(number) == number:
        return None
    return number - int(number)
``` 

In this modified version, if the number is not a valid floating-point number or is already an integer, the function returns `None`. Otherwise, it proceeds with the truncation logic to return the decimal part.