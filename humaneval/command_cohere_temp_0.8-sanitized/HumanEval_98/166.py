def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # Use a dictionary to store the number of uppercase vowels in even indices.
    # Initialize it to 0 for each vowel.
    d = { 'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0 }
    # Iterate through the string characters.
    for i, char in enumerate(s):
        # Check if the character is an uppercase vowel.
        if char.isupper() and char in 'AEIOU':
            # If the character is in an even index, increment the count.
            if i % 2 == 0:
                d[char] += 1
    # Return the count for all uppercase vowels in even indices.
    return sum(d.values())