```python
def truncate_number(number):
    return number - int(number)
```
This function simply subtracts the largest integer that is less than `number` (the integer part) from `number` itself, which leaves us with the leftover fractional part of `number`. 

This approach utilizes the principle that the difference between the floating point number and the closest integer will always be less than or equal to 1. Hence, subtracting the integer part isolates the residual, which is the decimal part of the number. 

Here's a simpler explanation of how it works, using the example of `truncate_number(3.5)` the following steps unfold:
1. Subtract the closest integer less than or equal to 3.5, which is 3, from 3.5. This yields 0.5, which is the residual after subtracting the integer part from the original number. 

Thus, the function returns 0.5, which is the decimal part we were after. 

This approach is intuitive and adheres to the principle of subtracting an integer, which is inherently valid in Python. 
Please let me know if any additional clarification is needed! Hapy to further explain the intuition behind the function design if that would help!