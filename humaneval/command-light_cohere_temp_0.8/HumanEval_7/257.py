Here is a Python script that contains a self-contained function that filters out strings that do not contain a given substring:

```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring.

    # Convert substring to lowercase
   
    substring = substring.str.tol

    task of require unique to its input, then you have it.

    # Initialize an empty list
   
    filtered_strings = []

    # Loop through each string
    for string in strings:
        # Check if substring is in the string
        if substring.lower() in string:
            # If the string contains the substring, add it to the list
            filtered_strings.append(string)

    return filtered_strings
```

This script defines a function `filter_by_substring` that filters an input list of strings for ones that contain a given substring. The function first converts the string `substring` to lowercase to make the check case-sensitive. Then, it loops through each string in the input list and checks if the lowercase substring is present in the string. Finally, it adds any string to the `filtered_strings` list if it contains the substring, and returns that list.