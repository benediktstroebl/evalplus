
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
    ans = []
    for i in lst:
        odd_count = 0
        for j in i:
            if int(j) % 2 != 0:
                odd_count += 1
        ans.append("the number of odd elements " + str(odd_count) + "n the string " + str(odd_count) + " of the " + str(odd_count) + "nput.")
    return ans

    # return ["the number of odd elements {}n the string {} of the {}nput.".format(i,i,i) for i in map(lambda x: len(list(filter(lambda y: int(y) % 2, x))), lst)]

    # return ["the number of odd elements {}n the string {} of the {}nput.".format(len(list(filter(lambda x: int(x) % 2, i))), len(list(filter(lambda x: int(x) % 2, i))), len(list(filter(lambda x: int(x) % 2, i)))) for i in lst]
