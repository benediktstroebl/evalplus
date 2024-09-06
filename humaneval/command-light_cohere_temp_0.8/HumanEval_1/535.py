```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    This function takes a string with parentheses and other containers like curly and square braces
    and returns a list of its independent, well-formed parts.
    """
    open the manually, to make it consistent and easy to read.
    """ Use the style with balanced and nested open and close parentheses.
    """
    following the value, you can create any test you wish and it will pass.
    """
    list of any space-separated and nested strings.
    """
Example:
    ```test_string = '() (( )) (( )( ))'
    ```
    """

    def split(match):
        groups = match.groups()
        # match.open isbalanced '()', ')'
        return '('.join(groups) + ')'

    string = "".join open()
    stack = [0]  # to keep track of the current index

    while string:
        mo = string.finditer(r'\()[0])  # find next match
        if mo:
            matched = split(mo)
            string = string.replace(matched, ' ')  # skip characters between containers
            stack.append(len(len(matched) + 1))  # increase index
        else:
            break

    return list(stack)
``` 
The above code defines a function `separate_paren_groups` that takes a string as input and returns a list of its independent, well-formed parts. The code uses the style with balanced and nested open and close parentheses to make it consistent and easy to read.

Please note that this solution is not efficient and might not work well for very large inputs, and there are more advanced and optimized algorithms for this problem.