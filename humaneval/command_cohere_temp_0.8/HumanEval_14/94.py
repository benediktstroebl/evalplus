```python
import re
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    prefixes = []
    current_prefix = ''
    for char in string:
        current_prefix += char
        prefixes.append(current_prefix)
    return prefixes
```

The code uses a loop to iterate through each character in the string. For each character, it appends it to the current prefix and then adds the current prefix to the list of prefixes. Once the loop completes, the list of prefixes from the shortest (the empty string) to the longest will be returned. 
To test this, you can run the following code:
```python
test_string = 'abc'
expected_output = ['a', 'ab', 'abc'] 

print(expected_output == all_prefixes(test_string))
```
The output should be:
```
True
```

This would prove that the function is working correctly.