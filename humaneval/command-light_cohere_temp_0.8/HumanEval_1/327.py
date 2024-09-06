Here is a Python script with a self-contained function that solves the problem of separating and balancing parentheses:
```python
from typing import List

def separate_paren_groups(string: str) -> List[str]:
    """
    Function to separate and balance parentheses. Returns a balanced string of groups of parentheses.
    """
    string = string.split('() ')
   
    balanced_str = ''
    for match in string.match('(\([^]+\))', balanced_str += match[0] + match[-1])
    balanced_str = balanced_str.split('() ')
    balanced_str
    return balanced_str.matches = []
    balanced_str.split('() ') 
    return matches
```
This function splits the input string into individual groups of parentheses, then splits each group into an open and closed parenthesis, and finally joins all the groups back together to form a balanced string of parentheses. The function also returns a list of all matches found in the string.