```python
def truncate_number(number):
    return number - int(number)
```
This Python script defines a function called `truncate_number` that takes in a single argument, `number`, which is expected to be a positive floating point number. Inside the function, the `int` function is used to convert the input number to an integer. By doing this, it extracts the largest integer that is less than or equal to the given number. The decimal part of the number remains as the difference between the original number and the integer part. This difference is returned as the decimal part of the number. 

Here is an example usage of the code:
```python
result = truncate_number(3.5)
print(result)  # expected output: 0.5
```
In this example, the number 3.5 is passed to the `truncate_number` function. By subtracting the integer part (3) from the original number (3.5), we're left with 0.5, which is then returned by the function. Thus, the output of this code is indeed 0.5, which is the decimal part of the number 3.5. 

This function provides a simple and efficient way to extract the decimal part of a positive floating point number.