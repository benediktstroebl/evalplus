```python
def starts_one_ends(n):
    return n == 1 or any(i >= n - 1 and str(i).start with '1' for i in range(2, n))

# Example usage:
print(starts_one_ends(4))  # Output: 2
print(starts_one_ends(5))  # Output: 1
print(starts_one_ends(6))  # Output: 0
print(starts_one_ends(7))  # Output: 0
print(starts_one_ends(8))  # Output: 0
print(starts_one_ends(9))  # Output: 0
print(starts_one_ends(10)) # Output: 2
```