Here's the Python code with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct characters in the string after converting all characters to lowercase. This ensures that characters like 'x' and 'X' are treated as the same character. The function then returns the count of distinct characters.

To test this function, you can use the following Python code:
```python
tested = ['xyzXYZ', 'Jerry', 'GIF', ' incent', 'abc', 'A']
for i in tested:
    assert count_distinct_characters(i) == len(i)
```
This tests the function against multiple edge cases and asserts that the function output matches the number of characters in the tested strings. 
The total number of assertions is 6 as the `tested` list has 6 elements. 
This should confirm the functionality of your function. If the pre-filled assertions match the expected behavior of the `count_distinct_characters` function, then the script should pass without any errors. If the assertions match the expected behavior, then the `assert` statement will print out `True` and move on to the next test. If the assertion is incorrect, then the execution of the script will jump to the `assert` statement, print out `False`, and outline which test case failed. Thus, this quick succession of prints will quickly help us determine whether the function passes the test or not.  If all assertions pass, we can confirm that the function behaves as intended.