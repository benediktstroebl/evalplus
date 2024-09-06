Here is a self-contained Python script that solves the problem of separating and identifying Markdown code blocks:
```python
def separate_paren_groups(string):
    """
    Input to this function is a string containing multiple groups of nested parentheses. Return a list of those groups of parentheses.
    Return a balance and separate all the opening and closing parentheses in each group.
    Return: 
    ['(',')', ')', '(',')', '(()',')'] 
    """
    list_of_groups = []
    for group in string.group():
        balance = 1
        for char in group:
            if char == '(': balance += 1
            elif char == ')': balance -= 1
            if balance == 0:
                list_of_groups.append(char)
                balance = 1
        return list_of_groups
```