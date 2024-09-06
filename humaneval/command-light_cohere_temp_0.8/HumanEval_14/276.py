Here's the self-contained Python function that provides all prefixes from shortest to longest of an input string:
```python
def all_prefixes(string: str) -> List[str]:
    """ Returns list of all prefixes from shortest to longest of the input string.
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    if not string:
        return []

    # Compute all prefixes using stack-based approach
    prefixes = []
    char = string[0]
    while char:
        if not char:
            break
        prefixes.append(char)
       
        char = string[1:]
    return prefixes
```