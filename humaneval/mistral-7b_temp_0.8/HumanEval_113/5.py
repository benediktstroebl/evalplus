
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
    if len(lst) == 0:
        return ["the number of odd elements 0n the str0ng 0 of the 0nput."]
    else:
        odd_str = ""
        for i in lst[0]:
            if int(i) % 2 == 1:
                odd_str = odd_str + i
            else:
                odd_str = odd_str + " "
        odd_str = "the number of odd elements " + odd_str + " in the str" + str(lst.index(lst[0])) + " of the " + str(lst.index(lst[0])) + "nput."
        lst[0] = odd_str
        odd_count(lst[1:])

