```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.find(substring) != -end]
# Run the function with the test cases
print(filter_by_substring([], 'a')))          # Output: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))) # Output: ['abc', 'bacd']
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'd')))  # Output: []
print(filter_by_substring(['abc', 'abcde', 'de'], 'abcde')) # Output: ['abcde']
``` 
This Python script defines a function `filter_by_substring` that filters a list of strings based on whether the substring is present within each string. The function uses the certain list of strings and a substring as input, and it returns a new list containing only the strings that contain the given substring. The test cases showcase how the run the function and verify its correctness.