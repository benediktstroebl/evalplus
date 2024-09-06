
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
    # loop over the list of strings, updating the sum variable
    # for each string
    # for string in lst:
    #     total = 0
    #     for i, digit in enumerate(string):
    #         if int(digit)%2 != 0:
    #             total += 1
    #     lst[lst.index(string)] = total
    # return lst
    # make a list of the list index positions of each string in lst
    # then loop through at the indices
    # for index in lst_index:
    #     for i, num in enumerate(string):
    #         if i%2 != 0:
    #             num = 0
    # return lst

    return [str(len([x for x in lst if int(x)%2 !=0])) + 'n the str' + str(lst.index(string)) + ' of the ' + str(lst.index(string)) + 'nput.' for lst_index, string in enumerate(lst)]
