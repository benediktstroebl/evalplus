```python
def how_many_times(string, substring):
    return len(string) - len(string.replace(substring, ''))
```

This function calculates the number of times the `substring` appears in the `string` by taking advantage of the fact that `replace()` removes the `substring` from the `string` while keeping the order of the characters intact. The `len()` function is then used to calculate the difference in length before and after the replacement operation. 

Would you like to know more about this approach? Or perhaps you'd like to delve deeper into tackling this problem using other algorithms? Please let me know your preferences, and I'll be glad to provide further insights. Let's proceed to test this script to ensure its effectiveness.

Here's a simple test suite to verify the correctness of the `how_many_times` function:
```python
# Test case with empty string
string = ''
substring = 'a'
expected_result = 0
result = how_many_times(string, substring)
assert result == expected_result, f"Expected {expected_result}, but got {result} for empty string"

# Test case with single instance of substring
string = 'aaa'
substring = 'a'
expected_result = 3
result = how_many_times(string, substring)
assert result == expected_result, f"Expected {expected_result}, but got {result}"

# Test case with multiple instances of substring
string = 'aaaa'
substring = 'aa'
expected_result = 3
result = how_many_times(string, substring)
assert result == expected_result, f"Expected {expected_result}, but got {result}"
```

This test suite covers multiple scenarios, including an empty string, a single instance of the substring, and multiple instances. The `assert` statements check if the actual result of the `how_many_times` function matches the expected result for each case. 

This should help confirm the expected behavior of the function. Let me know if you have any questions or if you'd like to further explore the subject of string manipulation or other concepts related to Python programming!