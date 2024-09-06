
def odd_count(lst):
    """Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "the number of odd elements in the
    string i of the input." where all the i's should be replaced by the number
    of odd digits in the i'th string of the input.

    >>> odd_count(['1234567'])
    ["the number of odd elements 4n the str4ng 4 of the 4nput."]
    >>> odd_count(['3',"11111111"])
    ["the number of odd elements 1n the str1ng 1 of the 1nput.",
     "the number of odd elements 8n the str8ng 8 of the 8nput."]
    """
    odd_list = []
    for s in lst:
        s = str(s)
        l=0
        for c in s:
            if c in ['2','3','5','7','9']:
                l = l + 1
        odd_list.append(l)
    return [f"the number of odd elements {n}n the str{n}ng {l} of the {n}nput." for n,l in zip(lst,odd_list)]

import doctest