```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join() for i, char in enumerate(string, 1) if char.group(i)]
```
This Python code defines a function called `all_prefixes`, which returns a list of all prefixes in the string, from shortest to longest, using the `enumerize` function to iterate over each character of the string in order, starting from the second character. 
The `group` method is used to create a generator that returns all prefixes in the string, by checking each character's group (its position relative to the beginning of the string) and returning `char` if it's a character. 
This is a simple and efficient way to generate all prefixes in a string.