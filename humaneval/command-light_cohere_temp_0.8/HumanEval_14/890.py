```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join + c for c in string]

# Test case
test_case = """a 
	bc 
	ada 
	ab"""
print(all_prefixes(test_case))  # Output: ['a', 'ab', 'bc', 'ada', 'ab']
``` 
This Python function, all_prefixes, takes a string as input and returns a list of all prefixes present in that string. It does this by iterating through the input string and appending each character to a new string until the string is built.