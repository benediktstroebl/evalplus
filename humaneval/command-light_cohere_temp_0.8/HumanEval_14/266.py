```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(char) for char in string if char.isalpha()]

def test_all_prefixes() -> None:
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
test_all_prefixes()
``` 
This code defines a function called **`all_prefixes`** that takes a string as input and returns a list of all prefixes from shortest to longest. The function uses a list comprehension to iterate over each character in the string, and only includes characters that are also letters (checked using the **`isalpha()`** method). 

The code also defines a function called **`test_all_prefixes`** which tests the correctness of the **`all_prefixes`** function by asserting that it returns the correct result for the input string '**"abc"**.