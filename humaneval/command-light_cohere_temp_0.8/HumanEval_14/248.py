```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join().
    # break out the string into a list of characters
    char_list = list(string)
    # sort the characters in order of frequency, from most to least
    frequency = {}
    for c in char_list:
        if c in frequency:
            frequency[c] += 1
        else:
            frequency[c] = 1
    sorted_chars = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    return [char for char, _ in sorted_chars]
# Add tests
string1 = "abc"
assert all_prefixes(string1) == ['a', 'ab', 'abc']
string2 = "hello"
assert all_prefixes(string2) == ['h', 'el', 'hello']
string3 = "1234"
assert all_prefixes(string3) == ['1', '23', '1234']
 ``` 
This script defines a function that returns a list of all prefixes from a given string. It sorts the words and their frequency, sorts them, and returns the most frequent ones first.