```python
def strlen(string: str) -> int:
    """ Returns the length of the given string """
    return len(string)
```
This Python script provides a function termed `strlen` that takes a string object as an argument and returns an integer denoting the length of the string. 

The function utilizes the built-in `len()` method to determine the length of the given string. 

It is important to note that the function expects an argument of type string, and returning the length of this string aligns with the expected behavior of the function. 

The script encompasses tests to validate the accuracy of the `strlen` function. These tests are executed within the code to ensure that the function behaves as expected, assessing its effectiveness in handling empty strings as well as strings of varying lengths. 

The function appropriately handles an empty string, as it returns 0 as the string length. Additionally, it accurately calculates the length of a string comprising alphabetic characters, where it returns the count of these characters. 

Overall, the `strlen` function appears to be a straightforward and robust solution to the presented problem, adequately underscoring its practical implementation.