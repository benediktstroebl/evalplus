Here's a Python script with a self-contained function `generate_even_digits` that solves the problem:
```python
def generate_even_digits(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.
    """
    # Ensure a is the smallest number
    if a > b:
        a, b = b, a
        
    even_digits = []
    for x in range(a, b + 1):
        if str(x).strip('0').isdigit():
            if int(str(x)[0]) % 2 == 0:
                even_digits.append(x)
                
    return even_digits

# Test Cases
print(generate_even_digits(2, 8))  # [2, 4, 6, 8]
print(generate_even_digits(8, 2))  # [2, 4, 6, 8]
print(generate_even_digits(10, 14)) # []
```

This script defines the function `generate_even_digits` which takes two positive integers a and b as inputs. It checks if a is greater than b, then swaps them to ensure a is the smaller number. It initializes an empty list even_digits to store the even digits. It loops through the integers between a and b (inclusive) and checks if the first digit of the string representation of x is an even integer. If so, x is appended to the even_digits list. Finally, it returns the even_digits list.

The provided test cases demonstrate the correct operation of the function. Feel free to modify the test cases to validate the function's behavior against different scenarios. Let me know if you have any questions or if you'd like me to explain any part of the code in more detail!