
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    vowel_dict = {"a": "A", "e": "E", "i": "I", "o": "O", "u": "U"}
    count = 0
    for index, letter in enumerate(s):
        if index % 2 == 0 and letter.upper() in vowel_dict:
            count += 1
    return count

