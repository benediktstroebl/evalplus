```python
def truncate_number(n):
    return n if n > 1 else 0.5  #n
``` 
This function takes a number and checks if it's greater than 1. If the number is greater than 1, it returns 0.5. If the number is less, it returns the integer part of the number (the largest integer less than the number) and returns it.