
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # split string into a list of characters
    words = s.split()
    # initialize an empty list to store count
    count = []
    # loop through each word in the list
    for i in range(len(words)):
        # if the word is empty, skip it
        if not words[i]:
            continue
        # if the word is uppercase, increment the count
        if words[i].isupper():
            count.append(1)
    # return the count
    return count
