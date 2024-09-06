```python
def separate_paren_groups(input_string: str) -> List[str]:
    groups = []
    for match in re.org.finditer(input_string, '(( )?)+'):
        if match.group != '(':
            groups.append(match.group)
        string = match.group
        match.match.string = ')'

        match.groups.append(match.group)
        get, list of the opening parentheses and return the list of those strings.
```

The provided function 'separate_paren_groups' takes an input string and matches and separates the groups of parentheses. The function uses the regular expression '(( )?)+', which matches one or more groups of opening parentheses. The function stores each group of parentheses in a list and returns the list of those groups.