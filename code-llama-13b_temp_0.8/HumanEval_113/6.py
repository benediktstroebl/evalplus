
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
    # string = 'the number of odd elements '
    # for item in lst:
    #     count = 0
    #     for j in item:
    #         if int(j) % 2 == 1:
    #             count += 1
    #     string += str(count)
    #     string += 'n the str'+ str(count)
    #     string += 'ng ' + str(count)
    #     string += ' of the '
    #     string += str(count)
    #     string += 'nput.'
    # return string

    string = 'the number of odd elements '
    string_list = []
    for item in lst:
        count = 0
        for j in item:
            if int(j) % 2 == 1:
                count += 1
        string_list.append("the number of odd elements " + str(count) + 'n the str' + str(count))
        string_list.append(str(count) + 'ng ' + str(count) + ' of the ' + str(count) + 'nput.')
    return [''.join(string_list)]
