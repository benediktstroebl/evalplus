
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

    #print(f'Input {lst}')
    def odd_counter(string):
        odds = 0
        for char in string:
            if int(char) % 2 != 0:
                odds += 1
        return odds
    output = []
    for string in lst:
        #print(f'for string {string}')
        #print(f'odd counter returns {odd_counter(string)}')
        output.append(f'the number of odd elements {odd_counter(string)}n the str{odd_counter(string)}ng {odd_counter(string)} of the {odd_counter(string)}nput.')
    return output
