```python
def separate_paren_groups(s: str) -> List[str]:
    return [match.match('(\(\d+)+)', s) for match in re.match.group('(\(\d++)+', s)]
    ```

This code uses the `re` module to create a regular expression that matches the desired pattern. The `group()` function is then used to split the string into a list of substrings. The output is a list of balanced parentheses.