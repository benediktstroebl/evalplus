

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    return len(string.split(substring, maxsplit=1)[1])


for n, s in enumerate(SAMPLE_ANSWERS):
    if how_many_times(s, '1') == SAMPLE_ANSWERS_EXPECTED[n]:
        print(f'Test {n} successful!')
    else:
        print(f'Test {n} unsuccessful!')
        print(f'Expected: {SAMPLE_ANSWERS_EXPECTED[n]}, actual: {how_many_times(s, "1")}')
