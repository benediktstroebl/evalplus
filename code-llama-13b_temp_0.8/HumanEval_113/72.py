
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
    ans = []
    for i in range(len(lst)):
        temp = lst[i]
        temp = temp.replace("1", "n the str1ng ")
        temp = temp.replace("3", "n the str3ng ")
        temp = temp.replace("5", "n the str5ng ")
        temp = temp.replace("7", "n the str7ng ")
        temp = temp.replace("9", "n the str9ng ")
        temp = temp.replace("0", "n the str0ng ")
        temp = temp.replace("2", "n the str2ng ")
        temp = temp.replace("4", "n the str4ng ")
        temp = temp.replace("6", "n the str6ng ")
        temp = temp.replace("8", "n the str8ng ")
        temp = temp.replace("0", "n the str0ng ")
        ans.append(temp)
    return ans


    return ["{}{}{}n{}".format(len(filter(lambda x: int(x)%2 != 0, i)), " the number of odd elements in the string ", i, " of the input.") for i in lst]


