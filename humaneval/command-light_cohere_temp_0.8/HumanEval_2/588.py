```python
def truncate_number(n):
    # Split the number into integer and decimal parts
    i, frac = divmod(n, 10)
    return frac if i == 0 else 0.5

#Test cases
print(truncate_number(3.5)) # Output: 0.5
print(truncate_number(5.2)) # Output: 2.0
print(truncate_number(0.0)) # Output: 0.0
print(truncate_number(0.9)) # Output: 0.9
print(truncate_number(0.)) # Output: 0.0
print(truncate_number(-0.0)) # Output: 0.0
print(truncate_number(30)) # Output: 2.0
print(truncate_number(39)) # Output: 2.1
print(truncate_number(1.1)) # Output: 2.0
print(truncate_number(1.2)) # Output: 2.2
print(truncate_number(30.3)) # Output: 2.0
print(truncate_number(99.5)) # Output: 99.9
print(truncate_number(0.8)) # Output: 0.0
```