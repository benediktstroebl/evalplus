```python
def all_prefixes(string: str) -> List[str]:
    prefixes = [string[:i]+'%' for i in range(len(string)+1)]
    return prefixes[:-1]
```

The code leverages list comprehension to generate a list of prefixes for the input string with the help of a generator expression. The expression utilizes slicing to create prefixes of varying lengths, and the % marker indicates the truncation point. The final list excludes the input string itself, ensuring a list of prefixes from shortest to longest.

Here is an example usage of the code:
```python
print(all_prefixes('Hello'))
```

Expected output:
```
['H%', 'He%', 'Hel%', 'Hell%', 'Hello']
```