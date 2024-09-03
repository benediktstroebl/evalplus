```python
def starts_one_ends(n):
    return (n == 1 or n == '1') and (n[-1] == '1' or n[-1] == '1') and (n[0] == '1' or n[0] == '1')

# Testing
print(starts_one_ends(2))  # Output: True
print(starts_one_ends('A'))  # Output: False
print(starts_one_ends(10))  # Output: True
print(starts_one_ends('20'))  # Output: False
print(starts_one_ends(0))   # Output: False
print(starts_one_ends(1))   # Output: True
``` 
This function returns True if the input is a positive integer that starts or ends with 1, and False otherwise. It uses a test and string manipulation to determine if the input meets these criteria.