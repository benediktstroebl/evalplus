```python
def truncate_number(number: float) -> float:
    return number - int(number)
```

The `truncate_number` function takes a floating point number as input and returns the decimal part of the number by subtracting the integer part of the number. 

Here is an example usage of the function:
```python
result = truncate_number(3.5)
print(result)  # Output: 0.5
```

This would return 0.5 as the result, which is the decimal part of the original number 3.5. 

The code passes the given test, but it's important to note that the result will be 0 if the input is a whole number, i.e., if it has no decimal part.