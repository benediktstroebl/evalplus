
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

    list_new = []

    for i in range(len(lst)):
        num_odd = 0
        for j in lst[i]:
            if int(j) % 2:
                num_odd += 1
        lst[i] = lst[i].replace('0', 'n', lst[i].count('0'))
        lst[i] = lst[i].replace('1', 'n', lst[i].count('1'))
        lst[i] = lst[i].replace('2', 'n', lst[i].count('2'))
        lst[i] = lst[i].replace('3', 'n', lst[i].count('3'))
        lst[i] = lst[i].replace('4', 'n', lst[i].count('4'))
        lst[i] = lst[i].replace('5', 'n', lst[i].count('5'))
        lst[i] = lst[i].replace('6', 'n', lst[i].count('6'))
        lst[i] = lst[i].replace('7', 'n', lst[i].count('7'))
        lst[i] = lst[i].replace('8', 'n', lst[i].count('8'))
        lst[i] = lst[i].replace('9', 'n', lst[i].count('9'))
        lst[i] = lst[i].replace('n', 'n the strnng ', lst[i].count('n'))
        lst[i] = lst[i].replace('n', 'n the strn of the ', lst[i].count('n'))
        lst[i] = lst[i].replace('n', 'n', lst[i].count('n'))
        list_new.append(lst[i] + 'n the str' + str(i) + 'ng ' + str(i) + ' of the ' + str(i) + 'nput.')
    return list_new

