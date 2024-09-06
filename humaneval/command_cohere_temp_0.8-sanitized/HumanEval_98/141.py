def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # Ensure the string contains only alphabets and is lowercase
    s = s.replace(' ', '').lower()
    # Transform string to contain only vowels and digits
    # Thus filtering out chars '[^aeiouAEIOU]'
    s = re.sub(r'[^aeiouAEIOU]', '', s)
    # Splitting the string into list of chars
    char_list = s.split('')
    # Applying filter to remove odd indices
    char_list = char_list[::2]
    # Counting uppercase vowels
    return sum(1 for char in char_list if char.isupper() and char in 'AEIOU')