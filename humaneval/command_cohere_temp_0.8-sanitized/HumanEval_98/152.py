def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    # Define the vowels to consider: uppercase AEIOU
    vowels = set('AEIOU')
    count = 0
    for i, char in enumerate(s, start=1):
        if char.isupper() and char in vowels and i % 2 == 0:
            count += 1
    return count