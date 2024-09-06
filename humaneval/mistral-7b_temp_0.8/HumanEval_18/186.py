

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    # 1. Substring can be empty
    # 2. Substring is longer than original string
    # 3. Substring is not found
    # 4. Substring is found
    # 5. Substring is found more than once
    # 6. Substring is found several times in the same place

    # Pseudocode
    # s = string
    # sub = substring
    # counter = 0
    # while s.startswith(sub):
    #     counter += 1
    #     s = s[len(sub):]
    # return counter
    #
    # counter = 0
    # while sub in s:
    #     counter += 1
    #     s = s[s.index(sub) + len(sub):]
    # return counter

    # Counting Substring Occurrences: count(1,0)
    # http://bookshadow.com/weblog/2018/04/09/leetcode-count-substring-occurrences/
    # https://leetcode.
