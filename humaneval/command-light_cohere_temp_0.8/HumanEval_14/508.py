```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(string[i:]) for i in range(len(string)) if string[i] != '']

# Test the function with a string containing all single characters
test_string = ''.join(test_string)

# Test the function with a string containing all digits
test_string_digits = '123 456 789'

print(all_prefixes(test_string))
print(all_prefixes(test_string_digits))
``` 
This script defines a function all_prefixes that returns a list of all prefixes in a given string. The function uses a prefix technique, where it takes the input string and creates a prefix by extracting characters from it using slicing. The function then checks if the range starts from the beginning (i.e., index 0) or a slice of the string, excluding the last character.