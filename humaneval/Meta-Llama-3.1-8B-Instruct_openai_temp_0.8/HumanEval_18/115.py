### Counting Substring Occurrences
#### Method: KMP Algorithm with modifications for overlapping occurrences

```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to search for.

    Returns:
        int: The number of occurrences of the substring in the string.

    Example:
        >>> how_many_times('', 'a')
        0
        >>> how_many_times('aaa', 'a')
        3
        >>> how_many_times('aaaa', 'aa')
        3
    """

    # Base case: If the substring is empty or the string is empty, return 0
    if not substring or not string:
        return 0

    # Initialize the count of occurrences to 0
    count = 0

    # Compute the failure function for the substring
    failure = [0] * len(substring)
    j = 1
    for i in range(2, len(substring)):
        while j > 0 and substring[i]!= substring[j]:
            j = failure[j-1]
        if substring[i] == substring[j]:
            j += 1
        failure[i] = j

    # Initialize the index to the start of the string
    i = 0
    for j in range(len(string)):
        # While the current character in the string does not match the current character
        # in the substring and we're not at the start of the substring, move back in the
        # substring based on the failure function
        while i > 0 and string[j]!= substring[i]:
            i = failure[i-1]
        # If the current character in the string matches the current character in the substring,
        # move forward in both the string and the substring
        if string[j] == substring[i]:
            i += 1
        # If we've reached the end of the substring, it's an occurrence
        if i == len(substring):
            count += 1
            i = failure[i-1]

    # Return the count of occurrences
    return count
```

This script uses the KMP (Knuth-Morris-Pratt) algorithm to efficiently find occurrences of the substring in the string. The modifications allow for overlapping occurrences to be counted correctly. The `failure` list is used to keep track of the longest prefix that is also a suffix for each substring starting at each position, allowing us to move backwards in the substring when there's a mismatch.