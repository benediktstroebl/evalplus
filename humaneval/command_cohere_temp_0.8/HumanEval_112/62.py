```python
def reverse_delete(s, c):
    # Resultant string after deletion of characters in s that appear in c
    result = ''.join(x for x in s if x not in c)
    # Check if the resultant string is a palindrome
    return result, result == result[::-1]
```

This approach uses Python's list comprehension and slicing to filter out characters from `s` that appear in `c`, and then checks if the resultant string is a palindrome. The returned value is a tuple consisting of the resultant string `result` and a boolean value indicating whether it's a palindrome (True if it is, False otherwise). 

To test this, you can run the following tests:
```python
# Test Case 1
test_string = "abcde"
characters_to_delete = "ae"
expected_result = ('bcd', False)
result = reverse_delete(test_string, characters_to_delete)
assert result == expected_result

# Test Case 2
test_string = "abcdef"
characters_to_delete = "b"
expected_result = ('acdef', False)
result = reverse_delete(test_string, characters_to_delete)
assert result == expected_result

# Test Case 3
test_string = "abcdedcba"
characters_to_delete = "ab"
expected_result = ('cdedc', True)
result = reverse_delete(test_string, characters_to_delete)
assert result == expected_result
```

This will ensure that the function performs the required operations correctly.