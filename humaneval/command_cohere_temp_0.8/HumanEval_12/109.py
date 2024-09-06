Here's a Python script with a self-contained function that solves the problem and includes corresponding tests:
```python
# The module where the longest function is defined
module = __import__('__main__', fromlist=['__name__'])

# The function that will be run during the test
def test_longest_function():
    # Empty list case
    assert module.longest([]) is None

    # Single item list case
    assert module.longest(['apple']) == 'apple'

    # Multiple items list case
    assert module.longest(['apple', 'banana', 'cherry']) == 'cherry'

    # Multiple items list case 2
    assert module.longest(['spongebob', 'patrick', 'squidward']) == 'squidward'

# Run the test case
test_longest_function()

# Function definition
def longest(strings: List[str]) -> Optional[str]:
    # Type hinting
    from typing import List, Optional

    # If the list is empty return None
    if not strings:
        return None
    # If there is only one string return it
    if len(strings) == 1:
        return strings[0]
    # If there is more than one string, return the longest one
    return max(strings, key=len)

# Conclusion of the script
print("All tests passed!")
```

The `longest` function is defined at the end of the script, it takes a list of `strings` as input and returns either `None` if the list is empty, the first string in the list if it contains only one item, or the longest string using the `max` function in case there are multiple strings. The `key=len` argument of the `max` function ensures that the strings are compared by their length. 

The `test_longest_function()` function is defined above the `longest` function and it tests the `longest` function against the test cases provided in the problem statement. It uses the `assert` statement to check that the actual output of the `longest` function matches the expected output for each test case.

When the script is run, the `test_longest_function()` function is called and the test cases are run, the script concludes by printing "All tests passed!" if all assertions passed.  This way, the code covers the functionality provided in the problem statement, and conveys its purpose clearly through the explicit function and test case naming.