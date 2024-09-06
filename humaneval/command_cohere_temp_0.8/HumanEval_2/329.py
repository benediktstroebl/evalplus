```python
def truncate_number(number: float) -> float:
    return number - int(number)
```

This function simply subtracts the largest integer that is less than the input number from the input number, which leaves us with the residual fractional part of the number, which is what we wanted. 

To elaborate on this method, consider the following example: 
- Let's say we have the floating-point number 3.75. Subtracting the closest integer, which is 3, from this number would give us 0.75, which is the residual part of the number after removing the largest integer component. 

This method is highly efficient, requiring only a single subtraction operation, and can be easily understood through its direct interpretation. 

Feel free to ask any follow-up questions!