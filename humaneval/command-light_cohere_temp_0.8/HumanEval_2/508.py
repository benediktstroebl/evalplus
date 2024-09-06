```python
def truncate_number(number: float) -> float:
    return number - (number // 10**9)  # removing decimal part
```
This function takes a number as input and returns the truncated decimal part of that number. It works by subtracting the decimal part of the given number. This decimal part is be calculated as the largest integer that is less than the given number, divided by 10**9. 

This function is a good candidate for solving the problem. 

This is a good starting point, and you can optimize or enhance it based on specific requirements or performance considerations.