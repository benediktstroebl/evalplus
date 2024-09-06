
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
    result = []
    for string in lst:
        if len(string) > 1:
            odds = ''
            if string[0] % 2 == 1:
                odds += '1'
            else:
                odds += '0'
            for i in range(1, len(string)):
                if string[i] % 2 == 1:
                    odds += 'n'
                else:
                    odds += ' '
            result.append("the number of odd elements {0}n the str{0}ng {0} of the {0}nput.".format(odds))
        else:
            result.append("the number of odd elements 0n the str0ng 0 of the 0nput.")
    return result

