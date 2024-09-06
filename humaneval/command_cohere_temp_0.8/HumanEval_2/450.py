```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than number from number itself. The decimals left in the difference will be less than 1, representing the desired decimal part of the number. 

To test this script, you can call the function with the example provided in the problem statement:
```python
truncate_number(3.5)
# Expected output: 0.5
``` 
This will return 0.5, which is the decimal part of the number 3.5. 

This approach is intuitive and simple to understand, making it a great choice for coding problems like this one. 
Let me know if you need anything else!