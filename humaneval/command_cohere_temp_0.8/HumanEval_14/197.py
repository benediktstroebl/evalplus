```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    prefixes = [string[:i]+('' if i == 0 else ' ') for i in range(len(string) + 1)]
    return prefixes
```

This script defines a function called `all_prefixes`, which takes a string as input and returns a list of all prefixes of the input string, from the shortest to the longest. The function uses a list comprehension to generate the prefixes using a for loop to iterate through the length of the string and adding single space if i is not 0 to separate the prefixes. It includes the empty string as the shortest prefix and adds a space to separate the prefixes. The output is a list of strings containing the input string's prefixes, ordered by length and separated by spaces.