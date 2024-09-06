
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # Initialize counter to 0
    count = 0

    # Iterate over even indexes
    for i in range(0, len(s), 2):

        # Check if letter is upper case
        if s[i].isupper():

            # If letter is uppercase add 1 to count
            count += 1

    return count
