from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    def prefix_length(s: str) -> int:
        """ Return length of the shortest prefix of the input string that matches the input string
        """
        for prefix in string:
            if s.startswith(prefix):
                return len(prefix)
        return 0

    prefix_length(string)
    prefixes = [string[i:].lower() for i in range(1, len(string)+1) if string[i:].lower() in string]
    return list(sorted(prefixes, reverse=True))
