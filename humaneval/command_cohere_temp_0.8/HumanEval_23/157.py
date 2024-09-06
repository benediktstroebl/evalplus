```python
def strlen(string: str) -> int:
    """ Returns the length of the given string """
    return len(string)
```
This Python script provides a function termed `strlen` taking a string argument and returning its length. The function utilizes the built-in `len` function to determine the length of the given string. 
```python
def test_strlen():
    """ Tests for the strlen function """
    assert strlen("") == 0
    assert strlen("abc") == 3
```
The accompanying test script comprises two assert statements to validate the functionality of the `strlen` function. These assertions verify that the length of an empty string indeed equals 0 and the length of the string "abc" is correctly assessed as 3. 
```python
test_strlen()
```
This statement invokes the test function `test_strlen`. Upon execution, the assert statements within the test function will evaluate the assertions. If all assertions pass, no error is raised, and the output of executing this script is None. Nevertheless, if any assertion fails, an assertion error is raised, and the output will entail particulars about the failure of the assertions during execution. This makes it possible to examine the correctness of the `strlen` function efficiently.