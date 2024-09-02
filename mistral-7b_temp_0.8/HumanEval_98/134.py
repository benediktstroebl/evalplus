
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # Your code goes here
    # length = len(s)
    #
    # # count = 0
    # for i in range(0, length, 2):
    #     if s[i] == 'A' or s[i] == 'E' or s[i] == 'I' or s[i] == 'O' or s[i] == 'U' or s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
    #         count += 1
    #         # print(i)
    # return count
    count = 0
    for i in range(len(s)):
        if i % 2 == 0 and (s[i].lower() in 'aeiou'):
            count += 1
    return count
