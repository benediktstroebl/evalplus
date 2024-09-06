```python
def truncate_number(number):
    return number - int(number)
```

The function takes in a `number` as input and returns the decimal part of the number by simply subtracting the integer part of the number. 

Here is a test case to verify the correct output:
```python
assert truncate_number(3.5) == 0.5
```

The above assertion will pass, verifying the correct output of the function.