```python
from typing import List

def separate_paren_groups(s: str) -> List[str]:
    return [p for p in s if not re.match(r'([')(.*? a(?!' + b)', ')+$')]
    ``` 
This function takes a string s, which may contain multiple groups of nested parentheses. It uses a `re.match` function to check if a pattern matches, which consists of any character except a ')', '(', or ')', followed by ')', followed by the balance of ')', and ending with a '$'. 

The `re.match()` function will returning a pattern, or any match found in the string, if not, it returns None. 

The function uses list comprehension to extract all the matched parentheses into a list of strings, and then returns that list. 
It will output a list of matched parentheses, which is as desired.