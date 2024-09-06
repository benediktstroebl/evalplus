```python
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    prefixes = [string[0]]
    for i in range(1, len(string)):
        prefixes.append(prefixes[i-1] + string[i])
    return prefixes
```
This function defines the all_prefixes method, which takes a string as input and returns a list of all the prefixes of this string, arranged from the shortest to the longest. It starts by initializing the list with the first character of the string (assuming a single-word input). It then iterates through the string, appending each character to the last prefix in the list, thereby creating longer and longer prefixes. Finally, it returns the list of prefixes, which includes the input string itself as the longest prefix, and any other prefixes ranging from the shortest (the first character) to the longest. 

Here is a sample test to see if the function is working properly:
```python
def test_all_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
```

The test code asserts that the function all_prefixes, when given the input 'abc', returns the expected output. The expected output is a list of three items: 'a', 'ab', and 'abc', which represents the three prefixes of the input string, arranged from shortest to longest. If the function works as expected, this test will pass. 

To run this test, you can use pytest (a popular testing library in Python): 
```bash
pytest -v
``` 

Or to run this specific test only, using python:
```python 
python -m pytest -v test_all_prefixes.py
``` 
The -v flag is used to enable verbose testing, which provides more information about the test run, making it easier to identify any failures. The python -m pytest command is used to execute the pytest function outside of the python environment, which is useful in command-line environments or when working with IDEs that don't have a python interpreter built in. Finally, test_all_prefixes.py is the file that should contain the test_all_prefixes function, assuming you have a single test in a file named as such.