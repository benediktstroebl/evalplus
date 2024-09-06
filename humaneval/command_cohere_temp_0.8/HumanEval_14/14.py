```python
def all_prefixes(string: str) -> List[str]:
    prefixes = [string[:i]+('' if i == 0 else '') for i in range(len(string)+1)]
    return prefixes
```

The task is to generate a list of all prefixes of the input string, ordered from shortest to longest. The solution uses a list comprehension that generates all prefixes of the input string, using a for loop to iterate through the length of the string and adding an empty string at the end to sharp the prefix. The output would look like this:
```bash
['a', 'ab', 'abc']
```