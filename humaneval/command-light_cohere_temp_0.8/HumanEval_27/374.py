Here is a Python script that contains a self-contained function that solves the problem of flipping the case of a given string:
```python
def flip_case(string: str) -> str:
    """
        Flip lowercase letters to uppercase and vice versa

        Parameters:
            string (str): The input string

        Returns:
            string (str): The flipped string
    """
    # Convert string to uppercase and return
    return string.make_upper() if string.isupper()
 value 

# Test the function
print(flip_case("hello"))  # Output: HELLO
print(flip_case("world"))  # Output: dOLLow
```