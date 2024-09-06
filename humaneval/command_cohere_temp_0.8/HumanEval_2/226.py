```python
def truncate_number(number):
    return number - int(number)
```

The `truncate_number` function takes a float number as input and returns the decimal part of the number. It does so by taking the difference between the given number and the largest integer less than or equal to the given number, as described in the prompt. 

Here is an example usage of the code:
```python
result = truncate_number(3.5)
print(result)  # Output: 0.5
```

This would return 0.5 as the output, which is the decimal part of the original number. 

The code provided seems to correctly answer the prompt's question and is logically sound. 

This script will only work correctly for positive input values. The value of the result will be negative if the input is a negative number.