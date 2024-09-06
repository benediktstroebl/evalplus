```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string while ignoring case and diaccounts.
    """
   
    specific character to not match
    """
    return sum(1 for i,c in enumerate(string.find(substring, case=False)))
```