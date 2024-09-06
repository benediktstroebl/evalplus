
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

    # reverse 
    lst_reverse = lst[::-1]

    odd_list = []
    # replace i with the number of odd elements in the i'th string of the input.
    for i in range(len(lst)):
        odd_count = 0
        # count number of odd digits in each string of lst_reverse
        for j in lst_reverse[i]:
            if int(j) % 2 != 0:
                odd_count += 1
        odd_list.append(odd_count)

    # now we reverse odd_list
    odd_list_reverse = odd_list[::-1]

    return [replace_i_with_odd_count_in_str(i, lst_reverse[i]) for i in range(len(lst))]

