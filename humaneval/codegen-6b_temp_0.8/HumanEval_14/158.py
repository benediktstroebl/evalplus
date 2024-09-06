from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # shorted_string will be one character longer than the input
    shorted_string = string[:-1]
    # suffix_list will be the p_list with prefixes
    suffix_list = []
    for i in range(len(shorted_string)):
        suffix_list.append(shorted_string[:i+1])
    
    return suffix_list

