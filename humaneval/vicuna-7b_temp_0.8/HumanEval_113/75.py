
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
    odd_count_lst = [0,1,2]
    n = 0
    for x in lst:
        for i in range(0, len(x)):
            odd_count_lst[n] += 1
            if odd_count_lst[n]%2 != 0:
                odd_count_lst[n] += 1
                if odd_count_lst[n] == 3:
                    odd_count_lst[n] = 0
    for i in range(1, len(lst)):
        result.append("the number of odd elements " + str(odd_count_lst[i-1]) + " in the string " + str(i) + " of the input.")
        if odd_count_lst[i-1] % 2 != 0:
            result.append("the number of odd elements " + str(odd_count_lst[i-1]) + " in the string " + str(i) + " of the input.")
            result.append("the number of odd elements " + str(odd_count_lst[i]) + " in the string " + str(i) + " of the input.")
    return result