from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # Define the string to search for prefixes in
    string = string.upper()
    # Initialize a list to store the prefixes
    prefixes = []
    # Iterate over all characters in the string
    for i in range(len(string)):
        # If the current character is a letter
        if string[i].isalpha():
            # If the current character is the first character of a prefix
            if i == 0 or string[i-1] not in string[i].upper(), prefixes.append(string[i-1]+string[i])
        else:
            prefixes.append(string[i-1]+string[i])
    # Sort the prefixes in ascending order
    prefixes = sorted(prefixes)
    return prefixes


if __name__ == "__main__":
    # Example usage
    print(all_prefixes('abc'))