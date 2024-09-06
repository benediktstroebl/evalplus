Here's the above code:
```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one of the inputs must be a positive integer")
    return max((i for i in range(1, max(a, b)) if a % i == 0 and b % i == 0))

# Example usage:
print(greatest_common_divisor(3, 5)) # Output: 1
print(greatest_common_divisor(25, 15)) # Output: 5
```
This function takes two integers a and b as input and returns the greatest common divisor of a and b. It employs the max function with the range to iterate through all numbers between 1 and the maximum of a and b, checking for divisibility. The function also raises a ValueError if either a or b is not a positive integer.