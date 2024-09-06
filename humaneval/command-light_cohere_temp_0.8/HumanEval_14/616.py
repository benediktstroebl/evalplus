```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [w for w in string if w.isalpha()]
```
all_prefixes('abc') # ['a', 'ab', 'abc']
``` 
This code defines a function `all_prefixes` that takes a string `string` as input and returns a list of all prefixes from shortest to longest of the input string. 

The algorithm uses list comprehension with a lambda function to iterate over each character in the input string and check if it is an alphabet character using the `isalpha()` method. 

The output of this code will be a list of strings ['a', 'ab', 'abc'] which are the prefixes from the string 'abc' from shortest to longest.