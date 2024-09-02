
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
    count_list = []
    for l in lst:
        str_list = list(l)
        sum_odd = 0
        for i in str_list:
            if int(i) % 2 != 0:
                sum_odd += 1
        count_list.append("the number of odd elements " + str(sum_odd) + "n the str" + str(sum_odd) + "ng " + str(sum_odd) + " of the " + str(sum_odd) + "nput.")
    return count_list
