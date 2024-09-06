
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

    # The number of odd digits in a string.
    def count_odd(string):
        odd = 0
        for c in string:
            if c in '13579': odd += 1
        return odd

    output = []
    for i in range(len(lst)):
        string = lst[i]
        output.append(f'the number of odd elements {count_odd(string)}n the str{count_odd(string)}ng {count_odd(string)} of the {count_odd(string)}nput.')
    return output
