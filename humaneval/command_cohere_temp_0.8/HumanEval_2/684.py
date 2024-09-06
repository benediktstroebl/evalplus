```python
def truncate_number(number):
    return number - int(number)
```

The `truncate_number` function takes a positive floating point number as input and returns the decimal part of the number. It does so by taking the difference between the given number and the closest integer (largest integer smaller than the given number) represented by the number, which effectively removes the integer part of the decomposition. 

Here is an example usage of the function:
```python
truncate_number(3.5)
# Output: 0.5
``` 

This will return 0.5 as the output, which is the decimal part of the number 3.5. 

This approach utilizes basic arithmetic operations to effectively extract the decimal part of a number, making it a simple and efficient solution.