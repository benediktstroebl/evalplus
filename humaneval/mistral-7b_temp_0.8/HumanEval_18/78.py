

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    # aaab -> aaab -> aaab -> 3
    # aaab -> aab -> 3

    # aaab -> aab -> 3
    # aaab -> aab -> 3
    # aaab -> aa -> 3
    # aaab -> a -> 3
    # aaab -> aaab -> 2
    # aaab -> aaab -> 2

    # aaab -> aa -> 2
    # aaab -> aa -> 2
    # aaab -> a -> 2
    # aaab -> aaab -> 1

    # aaab -> aaab -> 1
    # aaab -> aa -> 1
    # aaab -> a -> 1

    # aaab -> aaa -> 1
    # aaab -> aa -> 1
    # aaab -> a -> 1

    # aaab -> aaab -> 0
    # aaab -> aa -> 0
    # aaab
