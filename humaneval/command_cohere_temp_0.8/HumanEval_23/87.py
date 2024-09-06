```python
def strlen(s: str) -> int:
    """Returns the length of a string."""
    return len(s)
```

This Python script provides a function (`strlen`) that takes a string (`s`) as an argument and returns the length of that string. The function leverages the `len()` function, which is a built-in Python utility for determining the length of strings, lists, and other iterables. It's important to note that this function, `strlen`, is different from the `len` function, which is a keyword in Python and cannot be reused as a function name.

To ensure this function is working accurately, let's verify its behavior against a couple of test cases in a hypothetical scenario:
1. **Empty String Input**: If you pass an empty string to the `strlen` function, you would expect it to return zero (0) as the result.
2. **Non-Empty String Input**: For a non-empty string, such as "Hello," the `strlen` function should return the number of characters in the string, which is 5 in this case.

Therefore, if these expectations are met, you can confirm that the `strlen` function is operating as designed. You can then utilize it in your code to determine the length of any string you desire. 

Feel free to customize the function or add more tests specific to your requirements. If you have additional questions or need further assistance, please don't hesitate to ask!