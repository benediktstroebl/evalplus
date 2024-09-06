```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    return [p for p in s.format('() )() ()()')  # Test 1: balanced parentheses.
# Test 2: Unbalanced parentheses
s = '((()))'
result = separate_paren_groups(s)
print(result)  # Output: ['()', '())', '()()()']
``` 
This code uses the formatting technique known as **"curly braces to improve readability and avoid unbalanced parentheses"**. The code also uses the **List** from **typing** to build the result.