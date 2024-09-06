
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
    n = 1
    odd_count_list = []
    for i in range(len(lst)):
        if str(lst[i]).isdigit():
            lst[i] = int(lst[i])
            odd_count_list.append(str(n) + " odd elements in the " + str(i) + "th string.")
            n += 1
        else:
            odd_count_list.append(str(n) + " odd elements in the " + str(i) + "th string.")
            n = 1
            for k in range(i+1, len(lst)):
                lst[k] = int(lst[k])
            if len(lst) % 2 == 0:
                odd_count_list.append(str(n) + " odd elements in the " + str(i+1) + "th string.")
                n += 1
                for j in range(i+2, len(lst)):
                    lst[j] = int(lst[j])
                if len(lst) % 2 == 0:
                    odd_count_list.append(str(n) + " odd elements in the " + str(i+2) + "th string.")
                    n += 1
    return odd_count_list
