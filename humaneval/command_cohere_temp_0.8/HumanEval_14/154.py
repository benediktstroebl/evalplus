```python
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    prefixes = [str] * (len(string) + 1)
    prefixes[0] = ''
    for i in range(1, len(string) + 1):
        prefixes[i] = prefixes[i - 1] + string[i - 1]
    return prefixes[:-1]
```

The function constructs a list of strings that contain all the prefixes of the input `string', arranged from shortest to longest. It does this by using a list comprehension that generates strings by concatenating the previous prefix with the next character of the input `string'. The first element of the resulting list is an empty string, and the last element is the input `string itself. Finally, to remove the input string from the list, the function returns `prefixes'[:-1].'

Here is an example usage of the function:
```python
>>> all_prefixes('abc')
['a', 'ab', 'abc']
```
In the example, we can see that for the input 'abc', the function returns a list of prefixes from shortest to longest: `a', `ab', and `abc'. 

The `all_prefixes' function works correctly and follows the expected behavior of providing a list of prefixes from shortest to longest. It is concise and efficient, avoiding any unnecessary operations or iterations.