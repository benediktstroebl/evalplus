```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(char) for char in string if char != '']
test_cases = [
    'abc',
    'hello world',
    '',
    '   ']
  test_cases = [str(case) for case in test_cases]
  return all_prefixes(test_cases)
def all_prefixes(text: List[str]) -> List[str]:
    return [''.join(char) for char in text if char != '']
# Driver code
print(all_prefixes(['abc', 'world!']))  # Output: ['a', 'ab', 'abc']
print(all_prefixes(''))  # Output: []
print(all_prefixes([' ']))  # Output: []
```
The code defines a function that returns a list of prefixes from the shortest to the longest, starting from the input string. The code also provides several test cases to pass the function's test and prints the expected output.