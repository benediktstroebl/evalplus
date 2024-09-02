
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

    lst_ = []
    for elem in lst:
        count = 0
        for digit in elem:
            if int(digit) % 2 != 0:
                count += 1
        lst_.append(f"the number of odd elements {len(elem)}n the str{len(elem)}ng {len(elem)} of the {len(elem)}nput.")
    return lst_

