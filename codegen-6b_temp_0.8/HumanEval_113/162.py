
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
    def tally_odds(lst):
        """
        >>> tally_odds(['1234567'])
        [4, 2, 2, 2, 2, 0]
        >>> tally_odds(['3', "11111111"])
        [1, 0, 1, 0, 0, 0, 0, 0, 0]
        """
        tally = []
        for x in lst:
            count = 0
            for j in x:
                if int(j) % 2 != 0:
                    count += 1
            tally.append(count)
        return tally
    def n_odds(lst):
        """
        >>> n_odds(['1234567'])
        [4, 2, 2, 2, 2, 0]
        >>> n_odds(['3', "11111111"])
        [1, 0, 1, 0, 0, 0, 0, 0, 0]
        """
        tally = tally_odds(lst)
        total = 0
        for count in tally:
            total += count
        return total

    def result(lst):
        """
        >>> result(['1234567'])
        [4, 2, 2, 2, 2, 0]
        >>> result(['3', "11111111"])
        [1, 0, 1, 0, 0, 0, 0, 0, 0]
        """
        return [n_odds(lst)]

    return result(lst)
