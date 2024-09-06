```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This Python script defines a function called `filter_by_substring` which takes two parameters: `strings`, a list of strings, and `substring`, a single string. The function returns a new list containing only the strings from the input list that contain the specified substring. This is accomplished using a list comprehension, coupled with an in operator to check for substring presence. 
This solution adheres to the problem statement, and corresponding test cases should cover both empty input cases and valid ones where the substring is found in some strings. Pseudocode to outline the solution:
```python
# Input: A list of strings list_of_strings and a substring substring 

output_list = [] # Initialize an empty list called `output_list`

# Iterate over each string in the input list of strings
for string_item in list_of_strings:
    # Check if the substring is present in the string
    if substring in string_item:
        # If the substring is found, add the string to the `output_list`
        output_list.append(string_item)

# Return the filtered list of strings containing the substring
return output_list
``` 
This approach completes the filter_by_substring function, making sure the resulting solution is efficient and correctly handles all inputs.