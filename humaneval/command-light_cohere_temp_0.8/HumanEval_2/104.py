```python
def truncate_number(number: float) -> float:
    # use python's f-string to define the function
    return 1 / number if number > 1 else 0.0 if number else
 number
```
This code defines a function, `truncate_number`, that takes a number as an argument and returns the decimal part of that number. It does this by checking if the number is greater than 1, and if so, it returns 1 divided by the number; otherwise, it returns 0.0 if the number is not greater than 1, or the number itself if it is less than 1.