Here's a self-contained Python script that uses a technique called "rabin-karp algorithm" to find the number of times a substring can be found in the original string, including overlapping cases.

```markdown
# Find how many times a given substring can be found in the original string
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring can be found in the original string.
    """
    count = 0

    # Handle edge cases where substring is empty or string is empty
    if not substring:
        return 0

    # Handle edge case where substring is longer than string
    if len(substring) > len(string):
        return 0

    substring_hash = 0
    string_hash = 0
    h = 1

    # Calculate h value to be used for rolling hash
    for _ in range(len(substring) - 1):
        h = (h * 31) % 101

    # Calculate the initial hash values
    for i in range(len(substring)):
        substring_hash = (substring_hash * 31 + ord(substring[i])) % 101
        string_hash = (string_hash * 31 + ord(string[i])) % 101

    # Compare the hash values
    for i in range(len(string) - len(substring) + 1):
        if substring_hash == string_hash:
            # If the hash values match, compare the actual strings
            if string[i:i + len(substring)] == substring:
                count += 1
        if i < len(string) - len(substring):
            # Update the hash values for the next comparison
            string_hash = (string_hash - ord(string[i]) * h) % 101
            if string_hash < 0:
                string_hash += 101
            string_hash = (string_hash * 31 + ord(string[i + len(substring)])) % 101

    return count


# Example usage
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script uses the rolling hash technique to compare the hash values of the substring and the original string, and then compares the actual strings when the hash values match. The `h` variable is used to calculate the hash values, and it's calculated based on the length of the substring minus one. The `% 101` operation is used to prevent the hash values from getting too large. The script handles edge cases where the substring is empty or the original string is empty, and it also handles the edge case where the substring is longer than the original string.