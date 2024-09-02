
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
    res = []
    for num in lst:
        odds = [int(i) for i in num if int(i) % 2 != 0]
        res.append(num.replace('1', 'one').replace('2', 'two')
                   .replace('3', 'three').replace('4', 'four')
                   .replace('5', 'five').replace('6', 'six')
                   .replace('7', 'seven').replace('8', 'eight')
                   .replace('9', 'nine') + ' ' + str(len(odds)))
    return res
