
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # split the string into a list of characters
    # use a variable length list to store the vowels
    # use a variable length list to store the count of vowels in each index
    # iterate over the indices of the list
    # check if the character at the current index is a vowel
    # increment the count for the vowels in the current index
    # return the count of vowels in the current index
    vowels = 'aeiouAEIOU'
    vowel_count = [0] * (len(s) // 2 + 1)
    for i in range(len(s)):
        if s[i] in vowels:
            vowel_count[i//2] += 1
    return vowel_count
