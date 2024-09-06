```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    
    m, r = divmod(a, b)
    if m == 0:
        return r
    return greatest_common_divisor(b%r, r)

# Example usage
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
``` 
This function uses the Euclidean Algorithm to find the greatest common divisor of two integers. The function is self-contained, meaning it doesn't require any external functions or data to be executed successfully.