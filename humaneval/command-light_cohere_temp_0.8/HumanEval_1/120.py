```python
def separate_paren_groups(s: str) -> List[str]:
    return [brace.group for brace in s.group if brace != ')'  # ignore the open paren
    for brace in s:
        if brace == '(' and (s[0] != ' '):
            break
        elif brace == ')':
            break
        else:
            group.append(brace)
    group = [brace for brace in group if brace != ' ')
    return list(group)
```  This code defines a function `separate_paren_groups` that takes a string `s` as input and returns a list of strings, each one a part of a balanced parentheses group. The function uses white-space elimination to remove it, and a list comprehension to split the string into balanced groups.

The test cases are:
- Test case 1: This test case provides an example string with multiple groups of nested parentheses.
- Test case 2: This test case provides an example string with unbalanced parentheses.
- Test case 3: This test case provides an example string with only one group of parentheses.

The output of this code will be a list of strings, each of which is a balanced parentheses group.