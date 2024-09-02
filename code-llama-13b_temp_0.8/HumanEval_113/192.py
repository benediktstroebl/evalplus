
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

    def count_odds(string):
        """
        >>> count_odds('3')
        1
        >>> count_odds('11111111')
        8
        """
        count = 0
        for x in string:
            if int(x) % 2 != 0:
                count += 1
        return count

    string_lst = []
    for string in lst:
        string_lst.append(
            "the number of odd elements {}n the string {} of the {}nput.".format(
                count_odds(string), string, string
            )
        )
    return string_lst

