```python
def match_parens(lst):
    s = ''.join(lst)
    if len(s) % 2 == 0 and s.count('(') == s.count(')'):
        return "Yes"
    else:
        return "No"
```

The following test cases are included to verify correct function implementation: 

```python
# Test Case 1
test_list = ['()(', ')']
expected_output = "Yes"
assert match_parens(test_list) == expected_output

# Test Case 2
test_list = [')', ')']
expected_output = "No"
assert match_parens(test_list) == expected_output

# Test Case 3
test_list = ['((', '))']
expected_output = "Yes"
assert match_parens(test_list) == expected_output

# Test Case 4
test_list = ['((', '),(')']
expected_output = "Yes"
assert match_parens(test_list) == expected_output
```

This function accepts a list of strings, each containing only open or close parentheses, and returns a string indicating whether the two strings can be concatenated in some order to form a balanced parentheses string.