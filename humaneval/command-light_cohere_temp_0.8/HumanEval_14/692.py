Here's a self-contained Python function that returns a list of all prefixes from shortest to longest of the input string:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [w for w in string if not fuzzy(string, w)] 

def fuzzy(string, prefix): 
    """ Returns True if string starts with the prefix, else False """
    return prefix == string[0:len(prefix)]

# Example usage
print(all_prefixes('abc'))
```

This code uses the 'fuzzy' function to check if a prefix is a valid start of the string. This is efficient by using the previous prefix to check if the current prefix is a valid continuation or not.