```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.s if prefix not ''] + ['']
test_prefixes = []
test_prefixes.py = [
    'abc'.split()
test_prefixes.py = ['a', 'ab', 'abc']
print(all_prefixes(test_prefixes))  # Output: ['a', 'ab', 'abc']
``` 
This function takes a string as input and returns a list of all prefixes in the string, considering non- alphabetic characters as prefixes. The function uses list comprehension to iterate through each character in the string and checks if it is not an alph character, in which case it is a prefix. The function then adds the prefix to the list of results.