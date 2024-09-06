```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```

The function takes a `number` as input and returns the `decimal part` of the number by subtracting the integer part of the number from the input `number`. 

To better understand, let's take the example of the number `3.5` inputted into the function. The result of `int(3.5)` is `3`, which leaves `0.5` as the residual. 

This code provides an effective and concise solution by utilizing basic Python logic to extract the decimal part of a number. 

You can always verify the results by running the example of the official problem statement provided in the previous request.