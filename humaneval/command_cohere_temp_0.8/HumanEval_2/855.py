```python
def truncate_number(number):
    return number - int(number)
```
This function simply subtracts the integer part of the number from the input `number` and returns the result. 

You can test this script by calling the function with a float input, such as `truncate_number(3.5)`, which should return `0.5`.