```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    >>> separate_paren_groups(') )'
    Traceback (most recent call last):
      File "<string>", line 4, in separate_paren_groups
       ^ LINE DEBUG   File "<string>", line 4, in separate_paren_groups:
       ^ ^SyntaxError: ( ) expected in string 
	^```)
    >>> separate_paren_groups('( )( ) ( ) )')
    ['()', '()', '()']
    """
    result = []
    stack = [s]
    while stack:
        next_element = stack.pop()
       
            if next_element.count == 0:
            result.append(next_element)
        else:
            children = []
            while stack:
                current = stack.pop()
                if current.count == 0:
                    children.push(current)
                else:
                    children.push(current)
                    current.push(')')
            stack.push(current)
            stack.push('(')
            stack.append(')')
        result.append(next_element)
        stack = children
    return result
```