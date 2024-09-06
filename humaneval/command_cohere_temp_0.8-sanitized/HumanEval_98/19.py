def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    # Use a dictionary to store the count of each vowel in even indices.
    vowel_count = {upper_vowel: 0 for upper_vowel in 'AEIOU'}
    total_count = 0
    
    # Iterate over each character in the string.
    for char in s:
        if char.isupper() and char in vowel_count:
            vowel_count[char] += 1
    
    # Calculate the total count of uppercase vowels in even indices.
    for vowel, count in vowel_count.items():
        total_count += count * vowel_count[vowel]
    
    return total_count