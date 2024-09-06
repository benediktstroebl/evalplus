Here is a self-contained Python function that solves the problem you have described: 
```python
def all_prefixes(string: str) -> List[str]:
    """ Returns a list of all prefixes from shortest to longest of the input string.

    : Get string prefix of length 1: ''
    # Check for empty input
    if len(string) == 0:
        return []

    # Calculate the length of the string
    n = len(string)

    # Initialize prefixes list with empty strings of length n
    prefixes = [string[i:i+1] for i in range(n)]

    # Sort the prefixes by length from shortest to longest
    prefixes.sort()

    if len(prefixes) > 1:
        prefixes.sort(key = lambda x: len(x))

    return prefixes
```