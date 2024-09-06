```python
from typing import List
def separate_paren_groups(input_str: str) -> List[str]:
    pattern = r"\((.*?)\)"
    result = re.sub(pattern, r'\1', '', input_str)
    return [sub.split(' ', result) for sub in re.findall(pattern, result)]
``` 
This Python code defines a function `separate_paren_groups` that takes a single string as input, which may contain multiple groups of nested parentheses. The function utilizes regular expressions and string manipulation to:
- Define a pattern `r"\((.*?)\)"` to match any sequence of parentheses.
- Use the `re.sub()` method to replace the whole matched parentheses with an empty string.
- The resulting string is then split using `split(' ', result)` to separate each group of parentheses into separate strings.
- Finally, the function returns a list of these separated strings.