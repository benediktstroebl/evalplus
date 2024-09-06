```python
def truncate_number(number):
    return number - int(number)
```
This function simply subtracts the integer part of the number from the original number, which leaves us with just the decimal part. 

To test this script, you can call the `truncate_number` function with a float input value and compare the returned value with the expected output. 

For the provided example test case `3.5`, the expected output is `0.5`, since we want to return the decimal part of the number. 

The script should pass any tests that check the function's behavior for other valid input values as well.