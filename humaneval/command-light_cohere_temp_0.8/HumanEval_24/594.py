```python
def largest_divisor(n: int) -> int:
    return (n//3) + 1
``` 
This code calculates the largest divisor of a given number 'n' which is less than or equal to the original number and returns that largest divisor. 

It efficiently finds the large divisor using the formula n // d = d + 1, where n is divided by d, and d is the largest integer less than n that divides it evenly.