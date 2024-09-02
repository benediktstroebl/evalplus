
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
    # count_odd = [len([i for i in j if int(i) % 2 != 0]) for j in lst]
    # return ["the number of odd elements %s the str%sng %s of the %sinput."
    #         %(count_odd[i], i, count_odd.index(count_odd[i])+1, i+1)
    #         for i in range(0, len(lst))]

    return ["the number of odd elements %s the str%sng %s of the %sinput."
            %(len([i for i in j if int(i) % 2 != 0]), i, len(i), i+1)
            for i, j in enumerate(lst)]

