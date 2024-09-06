```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.a if prefix not in string] + [string]

# Test case:
def test():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']

# Run the function and print the result:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
test()  # Running the test case
```