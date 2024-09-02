
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
    odds_lst = []
    #for i in lst:
    #    odds_lst.append(n_digits(i))
    #return odds_lst

    len_lst = len(lst)
    for n in range(len_lst):
        count = 0
        for n in lst:
            if n[n] % 2 != 0:
                count += 1
        odds_lst.append(count)
    return odds_lst

