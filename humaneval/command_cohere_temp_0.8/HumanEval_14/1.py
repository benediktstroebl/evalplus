```python
def all_prefixes(string: str) -> List[str]:
    prefixes = [string[:i] for i in range(len(string) + 1)]
    return prefixes
```

This script defines a function `all_prefixes` that takes a string as an input and returns a list of all prefixes of the string, from the shortest to the longest. The function uses a list comprehension to generate the prefixes, taking care to include the empty prefix as well as the complete word itself.

Here is an example usage of the function:
```python
result = all_prefixes('abcdef')
print(result)  # Output: ['', 'a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef']
```

The output shows the list of prefixes for the input string, ranging from the empty string to the full 'abcdef' word.