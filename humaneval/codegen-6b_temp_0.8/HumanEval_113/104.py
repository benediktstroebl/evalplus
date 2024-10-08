
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
    list_of_odds = []
    for i in lst:
        number_of_odds = sum(1 for j in i if j in '1357')
        list_of_odds.append("the number of odd elements {}n the str{}ng {} of the {}nput.".format(number_of_odds, i, number_of_odds, i))
    return list_of_odds

