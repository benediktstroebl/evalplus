
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
    odds_list = []
    for word in lst:
        total = 0
        for char in word:
            if int(char) % 2 != 0:
                total += 1
        odds_list.append(total)

    return [f"the number of odd elements {x + 1}n the str{y + 1}ng {x} of the {y + 1}nput." for x, y in zip(odds_list, lst)]
