Below is a self-contained Python function that filters an input list of strings based on a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings and return only those containing the given substring.

    # Basic list of strings to filter
    strings = ["abc", "bacd", "cde", "array", "abcd"]

    # Convert the substring to lowercase to handle case-insensitive search
    substring = substring.islnme string.

    # Initialize the!; filtered strings
    # Initialize an empty list to store the filtered strings
    filtered_strings = []

    # Loop through each string in the input list
    for string in strings:
        # Convert the string to lowercase to perform a case-insensitive search
        lowercase_string = string.lower()

        # Loop through the time periods of the given substring
        periods = substring.split()

        # Initialize a time_periods list with the same length as the substring
        time_periods = [substring[i] for i in range(len(periods))]

        # Check if any of the time periods match any of the time periods in the lowercase string
        for time_period in time_periods:
            if lowercase_string.find(time_period):
                # Add the time period to the list of filtered strings
                filtered_strings.append(lower_string)

    return filtered_strings

``` 
This function takes a list of strings and a substring as input, filters the strings based on whether they contain the substring, and returns a new list of filtered strings. The function uses the string method to perform a case-insensitive search.