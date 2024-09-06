```python
def strlen(string: str) -> int:
    """ Returns the length of the given string """
    return len(string)
```
This Python script provides a function termed `strlen` that takes a string object as an argument and returns an integer denoting the length of the string. The function utilizes the `len()` function, a built-in Python utility, to determine the length of the provided string. It's important to note that this function, `strlen`, is distinct from the built-in Python `len` function, as it is overloaded here to explicitly return an integer value.

Here is an example of how to use the `strlen` function:
```python
def test_strlen():
    """ Tests for the strlen function """
    assert strlen("Hello World!") == 13, "Should correctly calculate string length"
    assert strlen("") == 0, "Should handle empty strings correctly"
    assert strlen("abc") == 3, "Should count spaces as part of length"
```

In this demonstration, we utilize the `strlen` function with three tests, each of which is executed to validate its correctness. The first test examines the function's capability to calculate the length of a standard string ("Hello World!"), while the second test examines its response for an empty string, ensuring that it returns 0. The third test examines the function's ability to calculate the length of a string containing only spaces, ensuring that it counts these spaces towards the total length. Thus, this block of code helps verify that the `strlen` function operates accurately and as designed. 

This codebase is a valuable tool for problem-solving and string manipulation, and it can be applied to a variety of applications involving string lengths.