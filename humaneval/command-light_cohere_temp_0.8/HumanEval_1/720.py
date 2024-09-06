Here is a self-contained Python script that defines a function named `separate_paren_groups`, which takes a string of parentheses as input and returns a list of strings that have been properly separated:
```python
import re
def separate_paren_groups(parentheses): 
    pattern = r"\(\[(.*?)\]"
    regex_matches = re.sub(pattern, parentheses, r'\1', '', parenthes)
    return list(regex_matches. 
# Example the following string as input: 
# '(( ( ) ) ) )'
# Expected output: ['( )', '()', '()()]' 
```

This script uses the `re` module to create a regular expression pattern that matches the desired parenthesis groups. The `sub()` method is then used to replace the matched parentheses with an empty string, effectively separating the groups. The `regex_matches` list is created by using `re.sub()` and returned to `parentheses` and contains the separate strings.