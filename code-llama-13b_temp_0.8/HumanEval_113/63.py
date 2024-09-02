
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
    for i in range(len(lst)):
        num = 0
        for j in lst[i]:
            if int(j) % 2 != 0:
                num += 1
        res.append(
            "the number of odd elements {0}n the str{0}ng {0} of the {0}nput.".format(i))
    return res

    # shorter
    # return [f'the number of odd elements {sum(1 for i in num if int(i) % 2)}n the str{i}ng {i} of the {i}nput.' for i, num in enumerate(lst)]

