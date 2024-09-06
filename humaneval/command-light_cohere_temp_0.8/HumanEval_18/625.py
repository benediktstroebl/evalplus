```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a given substring within the original string. 
    1. If the substring is has more than one character, the function returns 0.
    """
    pattern=re.sub(r'gcd', string)
    if len(pattern)==1: return 0
    return len(pattern)
```