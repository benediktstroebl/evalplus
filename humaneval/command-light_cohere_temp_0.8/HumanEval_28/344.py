```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Returns: combined string
    """
    return ''.join(strings)

# Test cases
my_list = ['a', 'b', 'c']
assertEqual(concatenate(my_list), 'abc')

my_string = 'hello world!'
concatenate(['world'])
assertEqual(concatenate(my_string), 'hello world! world!')

my_list2 = ['python', 'JavaScript', 'C++']
assertEqual(concatenate(my_list2), 'pythonJavaScriptC++')
```
This Python code provides a function `concatenate` that takes a list of strings and concatenates them into a single string. The test cases demonstrate the general usage of the function, passing in different lists of strings and verifying the expected output.