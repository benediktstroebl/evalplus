```python
def truncate_number(number):
    return number - int(number)
```

The `truncate_number` function takes a single parameter, `number`, which represents the positive floating point number to be truncated. It returns the decimal part of the number by subtracting the integer part of it. 

Here's an example usage of the function:
```python
result = truncate_number(3.5)
print(result)  # Output: 0.5
```

In the example, the integer part of `3.5` is `3`, and the decimal part is `0.5`. The function subtracts the integer part from the original number, leaving behind only the decimal part, which is then returned. 

This function simplifies the process of calculating the decimal part of a floating-point number, making it a useful tool for various mathematical and computational tasks. 

Remember to assert the input is a positive floating number, to ensure the output is always a decimal number too.