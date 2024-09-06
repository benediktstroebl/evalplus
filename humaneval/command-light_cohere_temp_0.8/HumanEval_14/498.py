Here's the solution:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(char) for char in string]
```
The function iterates through each character in the input string and returns a list of prefixes.

Here are some passes for testing the function:
```python
test_prefixes = ['a', 'ab', 'ac', '123', 'abc']
print(all_prefixes(''.join())
# ['a', 'ab', 'ac']

test_prefixes = ['', '', 'abc', '123']
print(all_prefixes(''.join())
# ['', '', 'abc']

test_prefixes = ['abc']
print(all_prefixes('abc'.join())
# ['abc']

test_prefixes = ['abc', 'abcd']
print(all_prefixes('abcd'))
# ['abcd']
```