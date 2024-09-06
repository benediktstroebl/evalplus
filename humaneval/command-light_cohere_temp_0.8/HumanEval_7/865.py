Here's the self-contained Python script that defines and utilizes the function `filter_by_substring`:
```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string. contains substring(string)]
```
The function uses the list comprehension to filter out strings from the input list that contain the given substring. It leverages the particular type of the `substrings` method, which returns a new string that is the same as the substring. This method is `substrings` method is passed as the `substring` argument, and the `strings` argument is passed as the list of strings to filter. The function then returns a list of strings that contain the given substring.