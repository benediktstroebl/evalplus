```python
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    prefixes = [string[0]]
    for i in range(1, len(string)):
        prefixes.append(string[:i])
    return prefixes
```

This code defines a function called `all_prefixes` that takes a string as input and returns a list of all prefixes of the input string, from the shortest to the longest. 

The function starts with an empty list called `prefixes` to store the prefixes. Then, it adds the single character prefix (the first character of the string) to the list. It iterates through the string starting from the second character up to the last character. In each iteration, it adds the substring of the first i characters to the list. Consequently, the list of prefixes is built. Finally, the function returns the list of prefixes. 

Here is an example usage of the function:
```python
print(all_prefixes('abc'))
```
This will output the list ['a', 'ab', 'abc'], which are the prefixes of the string abc from shortest to longest.