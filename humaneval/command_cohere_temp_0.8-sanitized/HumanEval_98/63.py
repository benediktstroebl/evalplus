def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # Use a dictionary to store the number of uppercase vowels in even indices encountered so far
    vowel_count = {True: 0, False: 0}
    # Iterate over each character in the string
    for i, char in enumerate(s):
        # Check if the character is an uppercase vowel
        if char.isupper() and char in 'AEIOU':
            # Check if the index is even and update the vowel_count
            if i % 2 == 0:
                vowel_count[True] += 1
    # Return the count of uppercase vowels in even indices
    return vowel_count[True]