
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """

    # check that all inputs are strings
    if not isinstance(s, str):
        return TypeError("Input must be a string.")

    # count how many upper case vowels are in even indexed letters
    counter = 0
    for index, letter in enumerate(s):
        if index % 2 == 0 and letter.isupper():
            counter += 1
    return counter
