
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

    def helper(lst):
        if len(lst) == 0:
            return []
        else:
            return ['the number of odd elements ' + str(count_odd(lst[0])) +
                    'n the str' + str(len(lst[0])) + 'ng ' + str(len(lst)) +
                    'n the ' + str(len(lst)) + 'nput.']

    def count_odd(string):
        count = 0
        for char in string:
            if int(char) % 2 != 0:
                count += 1
        return count
    return helper(lst)

