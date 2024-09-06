
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
    res = []
    for i in lst:
        temp = i
        n = 0
        while temp > 0:
            temp = temp // 10
            if temp % 2 == 1:
                n += 1
        res.append("the number of odd elements " + str(n) + " the str4ng " + str(i) + " of the " + str(lst.index(i) + 1) + " input.")
    return res