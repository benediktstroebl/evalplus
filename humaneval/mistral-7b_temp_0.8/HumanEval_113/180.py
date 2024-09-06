
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

    count = len(lst)
    odd = 0
    count_odd = 0

    if count == 1:
        if lst[0][0] == '1' or lst[0][0] == '2' or lst[0][0] == '3' or lst[0][0] == '4':
            odd += 1

        elif lst[0][0] == '5' or lst[0][0] == '6' or lst[0][0] == '7' or lst[0][0] == '8' or lst[0][0] == '9':
            odd += 2

    elif count >= 2:

        for i in lst:
            if i[0] == '1' or i[0] == '2' or i[0] == '3' or i[0] == '4':
                odd += 1

            elif i[0] == '5' or i[0] == '6' or i[0] == '7' or i[0] == '
