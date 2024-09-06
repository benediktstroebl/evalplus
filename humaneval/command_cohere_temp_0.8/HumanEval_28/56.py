```python
# Retrieve the requested function
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    result = ''
    for string in strings:
        result += string
    return result
```
The code uses a for loop to iterate over each string (`string`) in the provided list of strings (`strings`) and appends each string to an empty string called `result`. After processing all strings, the value of result is returned, resulting in a single string that concatenates all the provided strings. 

To run the code, you can create a new Python file and copy the code into it, or use an online Python interpreter and paste the code there. Once you execute the code, it will run the function with different test cases and print the results as plain text, which should match the behavior outlined in the docstring. 
If you face any issues in running the code locally, you can use an online Python interpreter like `https://www.repl.it/languages/Python` to experiment with small code snippets.