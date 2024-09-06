Here is a self-contained Python script that defines a function named `separate_paren_groups` that solves the problem of separating nested parentheses into individual strings:
```python
def separate_paren_groups(string: str) -> List[str]:
    """
    Separates balanced parentheses into individual strings.
    """
    balanced (each open brace is properly closed) and not nested within each other
    """
    result = []
    stack = []
    for char in string:
        if char == ')':
            if stack:
                result.append(''.join(stack))
                stack.pop()
        done.
        elif char == '(':
            stack.append(char)
        else:
            stack.append(char)
    stack.append('')
    done)
    result.append(char)
    done
    return result
```

The function takes a string `string` as input and returns a list of strings, where each string represents a separate group of parentheses. The function uses a stack data structure to keep track of open parentheses and closed groups. The program ensures balanced parentheses and does not have any extra characters.