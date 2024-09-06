
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # 1. Define a variable to track the number of uppercase vowels in even-indexed letters.
    count = 0

    # 2. Use enumerate() to iterate over the letters of the string,
    # 3. and increment count if the current letter is in uppercase and a vowel
    for index, letter in enumerate(s):
        if index % 2 == 0 and letter.isupper() and letter in 'AEIOU':
            count += 1

    # 4. Return the value of count.
    return count

