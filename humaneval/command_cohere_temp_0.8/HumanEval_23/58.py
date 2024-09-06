```python
def strlen(string: str) -> int:
    """ Return length of given string
    :param string: input string
    :return: length of the string
    """
    return len(string)
```

This Python script defines a function named strlen that takes a string as an argument and returns the length of that string. The function utilizes the built-in Python function len to compute the number of characters in the input string. 

To validate the correctness of the strlen function, two test cases are included. These test cases utilize Python's built-in unittest module to verify the function's behavior against expected outputs. 

To run the test cases, you can save the Python script into a file (for instance, strlen.py) and execute the file in your command line via `python strlen.py`. This will run the unittest and report on the number of assertions that passed, which should be two in this case. 

Please note that this script assumes that the tests are defined right within the same script as the `strlen` function. You can also have the tests defined in a separate file, which might be a more common practice in more complex projects. In that case, you would need to use the `unittest.main()` function to run the tests from that file.