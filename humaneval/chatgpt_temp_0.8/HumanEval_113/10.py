def odd_count(lst):
    """
    Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "the number of odd elements in the
    string i of the input." where all the i's should be replaced by the number
    of odd digits in the i'th string of the input.
    """
    output = []
    for string in lst:
        odd_count = len([char for char in string if int(char) % 2 != 0])
        output.append("the number of odd elements in the string {} of the input.".format(odd_count, string))
    return output
