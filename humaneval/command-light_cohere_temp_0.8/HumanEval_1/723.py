Here is a self-contained Python script that solves the problem you have provided:
```python
def separate_paren_groups(s):
    return [iclean(i) for i in s.clean((), '()', '(', ')')]


def iclean(i):
    # Regular expression to remove all non-braces
    return re.sub(r'\{[^,]+|\}+', '', i)
```
This function takes a string s as input and returns a list of strings with only the parenthesis, balanced and not nested. The regular expression [r'\{[^ ],]+|\}+'] is used to match any character that is not a braced.

The function also includes a shortcut for common and balanced parenthesis by using the '(' and ')' characters as a single string to be passed into the [str] list. 

This is just one possible for solving this problem, and you can further expand on this concept based on other patterns of balanced parenthesis.