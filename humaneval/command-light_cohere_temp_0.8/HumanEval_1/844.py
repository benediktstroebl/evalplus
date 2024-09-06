```python
def separate_paren_groups(input_string: str) -> List[str]:
    result = []
    for match in parser.search(r'\(\)\*(? coverage? wrap:',input_string, noc(',')):
        result.append(match.group())
   Is the Work a list of match objects, and the list of those match objects, in turn, is the list of separate parentheses groups, properly balanced and without any nested groups.