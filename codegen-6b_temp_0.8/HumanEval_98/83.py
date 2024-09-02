
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # Please print out which line of the above program contains the biggest 
    # number. If your code is correct, however, I'll have three numbers to 
    # consider:
    # 1. the number of uppercase vowels in even indices
    # 2. the number of uppercase vowels in odd indices
    # 3. the number of uppercase vowels in the entire string
    # Generally, the numbers in your count_upper program are greater than 1.
    #
    # See https://www.hackerrank.com/challenges/ctci-upper-lower-case
    # for the details of this problem
    count = 0
    for i in s:
        if i.isupper() and i.isalpha():
            if (ord(i) - ord('A') % 2) == 0:
                count += 1
    return count
