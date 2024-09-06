
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
    str_lst = []
    for i in range(len(lst)):
        odd_digit_count = 0
        if len(lst[i]) > 1:
            for j in lst[i]:
                if j%2 != 0:
                    odd_digit_count += 1
            str_lst.append("the number of odd elements " + str(odd_digit_count) + " in the " + str(i+1) + "nth string of the " + str(i+1) + "nput.")
        else:
            str_lst.append("the number of odd elements " + str(len(lst[i])) + " in the " + str(i+1) + "nth string of the " + str(i+1) + "nput.")
    return str_lst
