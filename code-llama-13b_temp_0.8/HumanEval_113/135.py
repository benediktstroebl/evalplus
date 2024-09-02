
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
    for lst_item in lst:
        if sum(int(d)%2==1 for d in lst_item) > 0:
            lst_item = lst_item.replace("1", "the number of odd elements 1n")
            lst_item = lst_item.replace("3", "the number of odd elements 3n")
            lst_item = lst_item.replace("5", "the number of odd elements 5n")
            lst_item = lst_item.replace("7", "the number of odd elements 7n")
            lst_item = lst_item.replace("9", "the number of odd elements 9n")
            lst_item = lst_item.replace("0", "the number of odd elements 0n")
            lst_item = lst_item.replace("2", "the number of odd elements 2n")
            lst_item = lst_item.replace("4", "the number of odd elements 4n")
            lst_item = lst_item.replace("6", "the number of odd elements 6n")
            lst_item = lst_item.replace("8", "the number of odd elements 8n")
            result.append(lst_item)
        else:
            lst_item = lst_item.replace("1", "the number of odd elements 0n")
            lst_item = lst_item.replace("3", "the number of odd elements 0n")
            lst_item = lst_item.replace("5", "the number of odd elements 0n")
            lst_item = lst_item.replace("7", "the number of odd elements 0n")
            lst_item = lst_item.replace("9", "the number of odd elements 0n")
            lst_item = lst_item.replace("0", "the number of odd elements 0n")
            lst_item = lst_item.replace("2", "the number of odd elements 0n")
            lst_item = lst_item.replace("4", "the number of odd elements 0n")
            lst_item = lst_item.replace("6", "the number of odd elements 0n")
            lst_item
