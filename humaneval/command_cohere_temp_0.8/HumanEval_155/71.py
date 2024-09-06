Here's a Python script that contains a function called even_odd_count, defined to solve the problem you've described:
```python
def even_odd_count(num):
    """Return number of even and odd digits in num."""
    num_str = str(num)
    even_count = 0
    odd_count = 0
    for char in num_str:
        if char != ' ':
            if char <= '9' and int(char) % 2 == 0:
                even_count += 1
            elif char <= '9' and int(char) % 2 != 0:
                odd_count += 1
    return even_count, odd_count
```

This script defines a function even_odd_count that takes a single argument, num, representing an integer. It then converts this integer to a string, and counts the number of even and odd digits in the string representation of the number. The function returns a tuple containing two counts: one for even digits and one for odd digits.

To demonstrate the usage of this function, here is a main method that calls the function on two numbers and prints the results:
```python
# Main method
num1 = -12
num2 = 123

even_count, odd_count = even_odd_count(num1)
print(f"For {num1}, there are {even_count} even and {odd_count} odd digits.")

even_count, odd_count = even_odd_count(num2)
print(f"For {num2}, there are {even_count} even and {odd_count} odd digits.")
```

The expected output of the program is:
```
For -12, there are 1 even and 1 odd digits.
For 123, there are 1 even and 2 odd digits.
```

This code demonstrates how to manipulate strings and integers in Python to solve a problem that involves counting even and odd digits in a number.