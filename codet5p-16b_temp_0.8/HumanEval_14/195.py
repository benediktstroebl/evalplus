from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """

    def all_prefixes_r(prefix: str, string: str) -> None:
        if len(string) > 0:
            prefixes = prefix + string[0]
            all_prefixes_r(prefixes, string[1:])
            print(prefixes)
        else:
            result.append(prefix)
    result = []
    all_prefixes_r('', string)
    return result
