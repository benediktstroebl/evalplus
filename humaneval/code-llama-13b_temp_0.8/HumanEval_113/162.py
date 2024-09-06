
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
    string = ''
    for i in lst:
        lst1 = i
        lst1 = lst1.replace("1", "the number of odd elements 1n the str1ng 1 of the 1nput.")
        lst1 = lst1.replace("3", "the number of odd elements 3n the str3ng 3 of the 3nput.")
        lst1 = lst1.replace("5", "the number of odd elements 5n the str5ng 5 of the 5nput.")
        lst1 = lst1.replace("7", "the number of odd elements 7n the str7ng 7 of the 7nput.")
        lst1 = lst1.replace("9", "the number of odd elements 9n the str9ng 9 of the 9nput.")
        lst1 = lst1.replace("0", "the number of odd elements 0n the str0ng 0 of the 0nput.")
        lst1 = lst1.replace("2", "the number of odd elements 2n the str2ng 2 of the 2nput.")
        lst1 = lst1.replace("4", "the number of odd elements 4n the str4ng 4 of the 4nput.")
        lst1 = lst1.replace("6", "the number of odd elements 6n the str6ng 6 of the 6nput.")
        lst1 = lst1.replace("8", "the number of odd elements 8n the str8ng 8 of the 8nput.")
        string = string + lst1
    return string
    
