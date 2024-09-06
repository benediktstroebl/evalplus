```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join[i for i, char in enumerate(string) if char != " "]]

#Test the function with a string that passes all tests
print(all_prefixes("abc"))
``` 
This script defines a function `all_prefixes` that returns a list of all prefixes from the shortest to the longest of the input string. 
The function uses a list comprehension to iterate over each character in the string and uses the condition `char != " "` to check if the character is not space.  

It then uses the list `join` to extract the character if it's not a space, creating the desired list of prefixes.