
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # s = 'dBBE'
    # vowels = ['a','e','i','o','u']

    # for index, letter in enumerate(s):
    #     if index % 2 == 0:
    #         if letter.lower() in vowels:
    #             return 1

    # return 0
    return sum(1 for index, letter in enumerate(s) if index % 2 == 0 and letter.isupper())

