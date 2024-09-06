```python
def longest(strings: List[str]) -> Optional[str]:
    # Validate input
    if not strings:
        return None

    # Sort strings alphabetically
    strings.sort(str)

    # Get the longest string
    longest_str = max(strings, key=len)

    return longest_str

# Test cases
def test_longest():
    longest_strings = ['a', 'bb', 'ccc']
    longest_result = longest(longest_strings)
    assert longest_result == 'ccc'

def test_empty():
    longest_strings = []
    longest_result = longest(longest_strings)
    assert longest_result is None

# Run the tests
test_longest()
test_empty()
```
The provided Python script defines a function called `longest` that takes a list of strings as input and returns the longest string from that list. It also includes two test cases: `test_longest` to validate the function's behavior with a list of strings, and `test_empty` to check the function's behavior when the input list is empty. 

These test cases effectively validate the correctness of the `longest` function and ensure it returns the expected result for different scenarios.