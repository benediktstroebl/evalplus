
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
    new_lst = []
    i = 0
    for str in lst:
        a = str.replace("1","1n the str1ng 1 of the 1nput.")
        b = a.replace("3","1n the str1ng 3 of the 1nput.")
        c = b.replace("5","1n the str1ng 5 of the 1nput.")
        d = c.replace("7","1n the str1ng 7 of the 1nput.")
        e = d.replace("9","1n the str1ng 9 of the 1nput.")
        f = e.replace("2","1n the str1ng 2 of the 1nput.")
        g = f.replace("4","1n the str1ng 4 of the 1nput.")
        h = g.replace("6","1n the str1ng 6 of the 1nput.")
        i = h.replace("8","1n the str1ng 8 of the 1nput.")
        j = i.replace("0","1
