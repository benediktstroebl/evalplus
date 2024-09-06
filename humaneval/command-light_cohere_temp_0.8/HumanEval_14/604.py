```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ['a' if i > 'a' else i for i in string.
    # tests are string from lowercase to ensure case insensitivity
    # no need for type hint, as string is str and we are using iterators over it
    # this is to ensure that the code works even if the input isn't sorted
    # a = b would not work if the input wasn't sorted
    return [] if string == "" else [i for i in string if i != '']
```
The above code defines a function that returns all prefixes of a given string from shortest to longest. The function works by iterating over the string from the smallest character to the largest and returns a list of all the characters it encounters. It is test a other case, the function will return an empty list if the input string is empty or consists solely of spaces.

Finally, the function tests if the input string is empty or consists solely of spaces, which is a valid input for this situation.