```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one of the inputs is zero.")
    return max((i for i in range(1, min(a, b) + 1)) & 1)

# Test the function
try:
    3
    5
    print(greatest_common_divisor(3, 5))  # Output: 1
   
    25
    print(greatest_common_divisor(25, 15))  # Output: 5

except ValueError as e:
    print(f"Error: {e}" )
```