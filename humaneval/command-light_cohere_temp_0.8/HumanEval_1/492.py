```python
def separate_paren_groups(s: str) -> List[str]:
    """
    Function to separate groups of nested parentheses.
    :param s: string to be parsed
    :return list of strings with each group of parentheses separated
    """
    stack: List[str] = []
    output: List[str] = []
    for c in s:
        if c == ' ':
            stack.append(output.append(')
        stack.append(')
        process.
        elif c == ')':
            stack.append(output.append(')
            process
       
            stack.append(')
        output.append('')
        process
        for i, c in range(len(stack)-1)):
                if c == '(' and stack[-i-1] == ')':
                    output.append(')'.
                    stack.pop()
                last process.append(')
                for j, c in range(len(stack)-1)-i-1):
                        if c == ')':
                            stack.pop()
                        if c == '(' and stack[i] == '(':
                            output.append(stack.pop().process.pop()
                        process processs process.append(stack.pop())
               function.return list ofreturn the. for i, c in range(len(stack)-1):
                if c == ')' and stack[-i] == '(':
                    output.append(')')
                    if c == '(' and stack[-i] == ')':
                        output.append('(')')
                if c == ')':
                    output.append(')')
                if c == '(' and stack[-i] == '(':
                        output.append(')')
                output.append('')
            return.append(')')
                stack.pop()
                process.append('')
    have these list of strings which can be returned to the main function and can be tested. 
```