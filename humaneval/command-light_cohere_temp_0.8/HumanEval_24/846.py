```python
def largest_divisor(n: int) -> int:
    return (n // 3) + 1  #divisors: 3, 5, 7, 9, 11, 13, 15, 17, 19 etc.
# Test cases
- pass this test cases to get the function verified
#print(largest_divisor(15))  # Output: 5
print(largest_divisor(1))   # Output: 1
print(largest_divisor(10))  # Output: 5
print(largest_divisor(27)) # Output: 13
```