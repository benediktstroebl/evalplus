
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
    str_ = "the number of odd elements "
    str1 = "n the string "
    str2 = " of the "
    str3 = "nput."
    result = []
    for i in range(0, len(lst)):
        odd = 0
        for j in lst[i]:
            if int(j) % 2 != 0:
                odd += 1
        result.append(str_ + str(odd) + str1 + str(odd) + str2 + str(odd) + str3)
    return result
