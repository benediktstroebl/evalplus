```python
def correct_bracketing(brackets):
    open_brackets = brackets.count("(")
    close_brackets = brackets.count(")")
    return open_brackets == close_brackets
```

This function counts the number of opening and closing brackets using the built-in `count` method. It then returns `True` if the counts are equal, indicating that every opening bracket has a corresponding closing bracket, and `False` otherwise. This solution is concise and straightforward, reflecting Python's idiomatic style.

Here is a Markdown code block containing a test for the function directly in the script:
```python
def test_correct_bracketing():
    assert correct_bracketing("()") == True
    assert correct_bracketing("(()())") == True
    assert correct_bracketing(")(()") == False
``` 

This test suite contains three tests, each checking a specific scenario against the function. This approach makes it very clear what scenarios are being tested, and gives a clear indication as to whether the function is working properly or not through the use of assert.