Here's a Python script that contains a function called even_odd_count that takes an integer num as input and returns a tuple with the number of even and odd digits respectively. This function is designed to solve the problem you've described:
```python
def even_odd_count(num):
    if not isinstance(num, int):
        raise ValueError("Input should be an integer")
    
    digits = str(num)
    count_even = sum(1 for digit in digits if digit in '02468')
    count_odd = sum(1 for digit in digits if digit in '13579')
    
    return (count_even, count_odd)

# Example usage
print(even_odd_count(-12))  # Output: (1, 1)
print(even_odd_count(123))  # Output: (1, 2)
```

This script will output the counts of even and odd digits as desired, handling the cases of negative numbers and multiple digits appropriately.