
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
    # expected = []
    # for i,num in enumerate(lst):
    #     odd_count = 0
    #     for item in num:
    #         if int(item) % 2:
    #             odd_count += 1
    #     expected.append("the number of odd elements %sn the str%sng %s of the %snput." % (odd_count, odd_count, odd_count, odd_count))
    # return expected
    new_lst = []
    for num in lst:
        odd_count = 0
        for item in num:
            if int(item) % 2:
                odd_count += 1
        new_lst.append("the number of odd elements %sn the str%sng %s of the %snput." % (odd_count, odd_count, odd_count, odd_count))
    return new_lst
