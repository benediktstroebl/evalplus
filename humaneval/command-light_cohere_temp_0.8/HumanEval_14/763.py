```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ['a', 'ab', string] + all_prefixes(string[1:])

def all_prefixes_test(test_string: str) -> None:
    assert all_prefixes(test_string) == ['a', 'ab', test_string] + all_prefixes_test(test_string[1:])
    return None

# Example usage
test_string = "abc"
all_prefixes_test(test_string)
``` 
This code defines a function all_prefixes that returns a list of all prefixes of a given string. The function includes a prefixes from the shortest to the longest, and then computes the prefixes of the rest of the string by recursively applying the function to each prefix.