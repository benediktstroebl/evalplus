Here's a self-contained Python function that calculates and returns the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)
```

You can use this function to get the length of any given string in Markdown format, for example:
```python
def test_markdown():
    input = """# Heading Martini...

    ---

    ${strlen}
    """
    print(strlen(input))
```

The output will be:
```
6
```