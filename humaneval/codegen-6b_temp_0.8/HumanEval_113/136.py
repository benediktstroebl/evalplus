
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
    count_odd = 0
    for i in lst:
        str_back = i[::-1]
        for j in range(0, len(str_back)):
            if int(str_back[j]) % 2 != 0:
                count_odd += 1
                break
    return ['the number of odd elements ' + str(count_odd) + 'n the str4ng ' + str(len(lst)) +
            ' of the ' + str(len(lst)) + 'nput.']


