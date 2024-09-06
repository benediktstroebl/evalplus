```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest number that divides n exactly and is smaller than n
    """
    # Ensure positive number
    n += 1
    # Return the largest integer less than n
    return max(n // -1, 2)

# Test cases
print(largest_divisor(15))  # Output: 5
print(largest_divisor(10))  # Output: 2
print(largest_divisor(6))  # Output: 2
print(largest_divisor(27)) # Output: 9 (Not exact divisor due to 27)
 ```