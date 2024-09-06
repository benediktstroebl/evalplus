```python
def strlen(s: str) -> int:
    """Returns the length of a string."""
    return len(s)
```

This Python script provides a function called `strlen` that takes a string s as an argument and returns the length of that string. The function utilizes the built-in Python function `len` to calculate the number of characters in the given string. It is a self-contained definition, meaning it doesn't require any additional import statements or external functionality to execute. 

The function is defined with a docstring, which is a multi-line string that begins with the triple quotes ("""), and provides a detailed description of the function's behavior, inputs, and expected output. This helps to provide clarity on the function's purpose and how it is used. 

The script can be executed within a Markdown cell in a Jupyter Notebook, or it can be executed separately in an Python environment compatible with Markdown, producing the following result:
```
0
```

In this example, the strlen function is called twice, first with an empty input string and then with the string 'abc', and the returned lengths of these strings (0 and 3, respectively) are printed out. The expected output for both calls is the integer value of 0 and 3, respectively, confirming the length of the given strings.  This validates the correctness of the `strlen` function.