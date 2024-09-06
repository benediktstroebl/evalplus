from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """

    # our result list
    result = []

    # iterate over the indices of our string
    for i in range(len(string)):

        # add the substring to result
        result.append(string[: i + 1])

    # return the result
    return result

