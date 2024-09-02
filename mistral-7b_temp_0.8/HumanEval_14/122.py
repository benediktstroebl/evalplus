from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """

    string = list(string)

    # Create a reverse copy of the string
    string.reverse()

    # Create empty result list
    result = []

    # Iterate through the string, starting from the last element
    for i in range(len(string)):

        # Create a prefix by concatenating the i characters from the end of the string
        prefix = "".join(string[:i + 1])

        # Append the prefix to the result list
        result.append(prefix)

    # Reverse the result list to get the desired order of prefixes
    result.reverse()

    return result

