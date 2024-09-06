```python
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    prefixes = [string[0]]
    for i in range(1, len(string)):
        prefixes.append(prefixes[-1] + string[i])
    return prefixes
```
This Python script defines a function called `all_prefixes` that takes a single argument, `string`, which is of type `str`. This function returns a list that contains all the prefixes of the input string, arranged in ascending order from the shortest (comprised of a single character) to the longest. 

The function begins by initializing an empty list called `prefixes` to store the generated prefixes. It then adds the single character prefix (the first character of the input string) to the list. Subsequently, it iterates through the input string, starting from the second character. During each iteration, the previous prefix is concatenated with the current character, creating a new prefix that is added to the list. This process is repeated until all prefixes, ranging from one character to the entire string, are included in the list of prefixes. 

The `all_prefixes` function provides a convenient way to obtain a comprehensive list of prefixes for any given input string, ensuring they are sorted in the order of their ascending length.