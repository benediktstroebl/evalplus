```python
def largest_divisor(n: int) -> int:
    return (n // 3) + 1
``` 
This function uses the `numerator_divisor` rule, which states that the largest number that divides a given number evenly is the largest number that can be multiplied by that number's divisors.  That fact- the findings for the largest number that divides n evenly, the function returns the largest number which is less than n and can be divided by n exactly.