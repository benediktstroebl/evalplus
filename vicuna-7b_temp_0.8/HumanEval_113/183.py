
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
    for i in range(0, len(lst), 2):
        odd = 0
        even = 0
        for j in range(i, len(lst)):
            if lst[j] in str(range(10))[:-2]:
                if lst[j] == str(range(10))[::-1][0][0]:
                    odd += 1
                else:
                    even += 1
        result.append("the number of odd elements %sn the str%sng %s of the 4nput." % (odd, even, i))
        odd = 0
        even = 0
    result.append("the number of odd elements %sn the str%sng %s of the 4nput." % (odd, even, len(lst) - 1))
    return result