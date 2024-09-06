```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string. contains.find(substring)]
 required_data = [['abc', 'bacd', 'cde', 'array', 'john doe'])
print(filter_by_substring(required_data, 'a'))
``` 
This code demonstrates a function that filters an input list of strings based on a given substring. It uses the required data with different strings and substring, and the function returns a new list containing only the strings that contain the substring. The code is a best practice of designing functions with descriptive names and using type hints for better readability and future-proofing.