```python
def separate_paren_groups(s: str) -> List[str]:
    """Separate groups of parentheses into separate strings."""
    return [p for p in s.split('() if p != '(']
```
This function splits the string around each parenthesis and discards the parentheses, effectively separating groups of parentheses into individual strings.