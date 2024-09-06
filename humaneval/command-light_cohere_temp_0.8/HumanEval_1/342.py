```python
def separate_paren_groups(s: str) -> List[str]:
    return [p.join(re.sub('([({|\)', ''), '')) for p,re in zip(['(', ')', ')', '()', ']', s.split('\n')]
by itertools. The regex [()] is used to capture each group of parentheses.

Here's a breakdown of what the function does:
1. First, the function uses the `re.sub()` function to replace all groups of parentheses with an empty string, effectively separating them.
2. Then, it uses the `zip()` function to go through each string and match the parentheses with the corresponding group.
3. For each match, it uses the `p.join()` function to extract the string before the group of parentheses.

The function effectively separates the groups of parentheses and returns the list of those strings.