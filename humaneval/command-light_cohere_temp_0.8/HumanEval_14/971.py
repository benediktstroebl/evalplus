```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string. string() if prefix else ''].
    """
### Function:
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string if prefix != '']  # returns list of all prefixes excluding '

### Test Cases:
```python
string = "abc"
print(all_prefixes(string))  # Output: ['a', 'ab', 'ac']

string = ""
print(all_prefixes(string))  # Output: []

string = "#$%^&*()"
print(all_prefixes(string))  # Output: ['#', '%', '^', '&', '!&']

string = "Lorem ipsum dolor sit amet."
print(all_prefixes(string))  # Output: ['Lorem', 'ipsum', '', 'sit', 'amet']
```  # This line prints 10 possible prefixes.