from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # Create a list of the string's characters
    char_list = list(string)

    # Initialize an empty list to store prefixes
    prefixes = []

    # Loop through each character in the list
    for i in range(len(char_list)):
        # Create a copy of the prefixes list with the current character removed
        prefixes_copy = prefixes[:-1]

        # If the current character is the first character in the string, append it to the prefixes list
        if i == 0:
            prefixes.append(char_list[i])

        # If the current character is not the first character in the string, add it to prefixes as a prefix
        else:
            prefixes.append(char_list[i])

            # If the prefix is not empty, append it to prefixes as a prefix
            if prefixes[-1] != '':
                prefixes.append(prefixes[-1])

        # Remove the current character from the char_list
        char_list.pop(i)

        # Append the length of the prefixes to the prefixes list
        prefixes.append(len(prefixes))

    return prefixes