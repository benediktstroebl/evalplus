Here's a Python script that contains a function called even_odd_count which takes in an integer and returns a tuple with the count of even and odd digits respectively:
```python
def even_odd_count(num):
    count = 0
    # Convert integer to string
    num_str = str(num)
    # Initialize the count of even and odd digits to 0
    even_count = 0
    odd_count = 0

    for char in num_str:
        if char > '9':
            # Character is larger than 9, it's an exponent or a character from NaN
            # Assuming these cases to be odd, as they are uncommon
            odd_count += 1
        elif char % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return (even_count, odd_count)

# Example usage
print(even_odd_count(-12))  # (1, 1)
print(even_odd_count(123))  # (1, 2)
```

This script defines the `even_odd_count` function, which takes an integer as input and returns a tuple containing the counts of even and odd digits in the number. The code converts the input integer to a string, then iterates through each digit, counting them while considering even and odd digits. The example usage demonstrates how the function operates and provides the expected outputs for the given examples.