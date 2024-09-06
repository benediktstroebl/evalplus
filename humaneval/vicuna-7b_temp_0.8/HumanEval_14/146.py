from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # Initialize empty list to store prefixes
    prefixes = []
    
    # Loop through characters in the string
    for char in string:
        # If string is empty or the current character is not a letter,
        # no prefixes can be formed from this string
        if len(string) == 0 or not char.isalpha():
            continue
        
        # Create an empty prefix list
        prefix_list = []
        
        # Loop through all characters in the string
        for i in range(len(string)):
            # If current prefix is empty, append the first character
            # to the prefix list
            if prefix_list == ['']:
                prefix_list.append(char)
                prefixes.append(prefix_list)
                prefix_list = []
            # Otherwise, append the current character to the prefix list
            # and check if it can be concatenated with the previous prefix
            else:
                prefix_list.append(char)
                if i > 0 and string[i-1].isalpha():
                    prefixes.append(prefix_list)
                    prefix_list = []
                    
    # Return the prefix list
    return prefixes

