```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]

# Test cases
strings = ['abc', 'bcd', 'cde', 'array', 'for', 'pi']
prefix = 'for' 

print(filter_by_prefix(strings, prefix))  # Output: ['for', 'pi']
``` 
This script defines a function called **filter_by_prefix** that filters an input list of strings based on a given prefix. 

It uses the **list comprehension** to iterate over each string in the input list and checks if the string starts with the given prefix. 

When this condition is met, the string is added to the output list.