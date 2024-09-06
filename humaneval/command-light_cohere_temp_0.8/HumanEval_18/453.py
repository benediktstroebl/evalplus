```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string.
    return sum(1 if string.find(substring) != -end else 0)
        for i,c in enumerate(string):
            if c==substring:
                return i+1
    return 0
```