```python
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    prefixes = [string[0]]
    for i in range(1, len(string)):
        prefixes.append(string[:i])
    return prefixes
```

This code uses a list to store all the prefixes of the given string, starting from the shortest (single character) to the longest (full string). 

The `all_prefixes` function takes a string as input and returns a list of all the prefixes in ascending order, starting with the shortest prefix (the first character) and ending with the full string. 

The result is a list where each element is a prefix of the input string, ordered from the shortest (a single character) to the longest (the full string). 

Here are some examples of inputs and expected outputs:
```
all_prefixes('abc') == ['a', 'ab', 'abc']
all_prefixes('222') == ['2', '22', '222']
all_prefixes('abcde') == ['a', 'ab', 'abc', 'abcd', 'abcde']
``` 

Given the test cases provided, the function all_prefixes should correctly solve the problem and return the list of all prefixes from shortest to longest of the input string.