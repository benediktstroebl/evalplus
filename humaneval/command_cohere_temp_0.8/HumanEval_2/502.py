```python
def truncate_number(number):
    return number - int(number)
```
This function simply subtracts the largest integer less than number, which is achieved by flooring the number, from the original number to leave behind the desired decimal part. 
Please note that the function signature has been modified to accept a plain number rather than a parameter with a specific type to improve code readability and flexibility.