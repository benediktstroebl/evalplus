```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(c) for c in string if c.isalpha()]
print(all_prefixes('abc'))
``` 
This Python code defines a function called **`all_prefixes`** that takes a string as input and returns a list of its prefixes. This is a function converts each character in the input string to lowercase using the **`lower()`** method, then iterates through each character using a **`for`** loop. The **`isalpha()`** method checks if each character is an alphabetic, and if so, it adds the lowercase version of that character to the list of prefixes.