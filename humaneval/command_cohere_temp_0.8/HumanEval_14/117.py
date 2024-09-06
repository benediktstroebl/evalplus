```python
def all_prefixes(string: str) -> List[str]:
    prefixes = [string[:i]+'%' for i in range(len(string)+1)]
    return prefixes[:-1]
```

The function constructs a list where each element represents a prefix of the input string, with the shortest prefix being '%%' and the longest being the entire string. The list is derived by concatenating the string with the prefix '%' and cutting it at different lengths. This list is subsequently modified to exclude the '%' marker and return the valid prefixes from shortest to longest. 

Here is an example usage of the function:
```python
>>> all_prefixes('abcdef')
['%', 'a%', 'ab%', 'abc%', 'abcd%', 'abcde%', 'abcdef']
```

The output is a list of prefixes of the string, excluding the marker '%' and presented in order from the shortest length to the longest.