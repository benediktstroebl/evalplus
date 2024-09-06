```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(char for char in string if char.isalpha()) for i in range(len(string) - 1)]
``` 
This function uses the List comprehension to iterate over each character in the string and filters out non-alph characters, then converts the filtered characters into a string using the join function and returns the list of all prefixes.