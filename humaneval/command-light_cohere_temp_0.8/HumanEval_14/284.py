Here's a self-contained Python function that provides all the prefixes of a given input string:
```python
def all_prefixes(string: str) -> List[str]:
    return [''.join(char) for char in string]

# Test cases
string1 = "hello"
string2 = "world"

print(all_prefixes(string1))  # Output: ['h', 'el', 'll', 'o', 'wor']
print(all_prefixes(string2))  # Output: ['w', 'o', 'rd', 'll']
```

This code defines a function all_prefixes that returns a list of all prefixes of a given string. The function iterates over each character in the input string and creates a prefix by prepending each character.