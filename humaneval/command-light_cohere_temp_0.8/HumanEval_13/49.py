Here is a self-contained Python script with a function that calculates and returns the greatest common divisor of two integers a and b:
```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("At least one of the inputs must be a positive integer")
    while a != 1 or b != 1:
        a, b = divmod(a, b)
    return a if a == 1 else b
```
This function takes two integers a and b as input and uses a while loop to calculate the greatest common divisor. The loop continues until either a numbers become 1, and the larger number is stored in the variable a (or b, depending on which is larger). 

This function then returns the larger number as the result.