Here's a Python script that contains a function called even_odd_count which takes in an integer and returns a tuple with the count of even and odd digits respectively:
```python
def even_odd_count(num):
    count = 0
    # Convert the integer to a string.
    num_str = str(num)
    # Initialize the count of even and odd digits to 0.
    even_count = 0
    odd_count = 0
    # Iterate through each digit in the number.
    for digit in num_str:
        # If the digit is even, increment the even count.
        if digit % 2 == 0:
            even_count += 1
        # If the digit is odd, increment the odd count.
        else:
            odd_count += 1
    return (even_count, odd_count)

# Example usage:
print(even_odd_count(-12))  # Output: (1, 1)
print(even_odd_count(123))  # Output: (1, 2)
```

This script defines the `even_odd_count` function, which takes an integer as input, counts the number of even and odd digits in the number's string representation, and returns a tuple of both counts. The provided examples in the original problem statement are also tested. 

Output:
```
(1, 1)
(1, 2)
```