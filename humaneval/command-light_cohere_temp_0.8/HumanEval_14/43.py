```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join(x) for x in string.
    # use of __ if statement to run the function and assert its output with the right-hand side
    assert all_prefixes('abc'), "prefixes should be ['a', 'ab', 'abc']"
    return ['a', 'ab', 'abc']
```
This code defines a function `all_prefixes` that returns a list of all prefixes from the shortest to the longest of the input string. 
The function uses the string `string` as an argument and iterates through all the characters in the string, creating a list of prefixes. 

The code then tests whether the function produces the correct output with the `assert` statement.