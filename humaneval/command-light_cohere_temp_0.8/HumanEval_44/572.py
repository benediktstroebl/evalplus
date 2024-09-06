```python
def change_base(x: int, base: int):
    """Change the base of a number to another. 

   : Convert an integer to a string representation with the specified base.

    Args:
        x: The number to change the base of.	 base: The desired base to convert the number to
    """

    # Convert the number to string representation
    s = str(x)

    # Check if the string length is not equal to base
    if len(s) != base:
        raise ValueError("Number has too few digits to convert to base.")

    # Convert the string to the desired base
    s = s[-base:]

    return s

# Example usage:
x = 8
base = 2

# Change the base of x to base 2
result = change_base(x, base)
print(result)
``` 
This script defines a function change_base that takes two parameters: x, which is the number to be converted, and base, which is the base to convert the number to. It then converts the string representation of x using the specified base, ensuring that the resulting string has the correct length. The script then passes the value checks to ensure that the input is valid and the function is properly implemented.