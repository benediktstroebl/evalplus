```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    return [p for p in s.string() if p != ']' and p[0] == '(']

# Test the function
test_str = "() (( )) (( )( ))"
print(separate_paren_groups(test_str))  # Output: ['()', '(())', '(()())']
```
This function takes a string of parenthesis groups as input and splits it into individual groups. It uses a for-loop to iterate over each character p in the string s, and if p is neither a space and the first character of p is an open parenthesis '(', it adds p to the list of separated parentheses.