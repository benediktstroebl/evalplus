Here's a solution to the problem:
```python
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # Use built-in prefix() to generate all prefixes
    # and remove the "" prefix
    return [prefix[1:] for prefix in string.prefix()
    trends to be a generator expression
    #     that yields the result of the function prefix(). Shaker's solution
    #     from prefix() would be to define a generator expression
    #     (by placing the generator in curly braces) and unpack
    #     it later, but that requires Python 3.4
    #     Instead, use a generator expression in Python 3.2
    """ use the his another approach to achieve the same result,
    that uses list comprehension.
```