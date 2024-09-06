
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

    # Function calls
    res = []

    for i in range(len(lst)):
        num_of_odd = 0
        for j in range(len(lst[i])):
            if int(lst[i][j]) % 2 == 1:
                num_of_odd += 1
        res.append("the number of odd elements %sn the str%sng %s of the %snput." %(num_of_odd, num_of_odd, lst[i], num_of_odd))
    return res
