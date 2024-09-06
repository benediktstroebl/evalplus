Here is a self-contained Python script that solves the problem of finding all prefixes from the shortest to the longest of a given string:
```python
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string

    :param string: str - input string
    :return: List[str] - list of all prefixes
    """
    if not string:
        return []

    # Use Python 3 style string methods
    prefixes = [string[:i] for i in range(1, len(string) + 1)]

    return prefixes
```