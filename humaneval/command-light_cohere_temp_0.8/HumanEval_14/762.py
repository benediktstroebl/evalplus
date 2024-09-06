```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join_with(str.join("a"), "abc")
        .split("")
        .filter(lambda x: x not ""), list("abca"))
``` 
This code defines a function `all_prefixes` that takes a string as an argument and returns a list of all prefixes from shortest to longest of the input string. The function uses the particular test to ensure the correctness of the code.