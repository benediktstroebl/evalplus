def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowels = 'aeiouAEIOU'
    
    # Extract substrings from the right half of the word.
    right_half = word[-len(word)//2:len(word)]
    substrings = right_half.split('')
    
    # Count vowels and consonants at the beginning and end of each substring.
    vowel_counts = [
        sum(1 for char in substring if char in vowels)
        for substring in substrings
    ]
    
    # Find indices of the closest vowel on either side of the word.
    left, right = float('inf'), float('-inf')
    for i, v in enumerate(vowel_counts):
        if v > 0:
            left = min(left, i)
        if v < 0:
            right = max(right, i)
            
    # Find the index of the closest vowel between two consonants.
    closest_index = min(left, right)
    
    return substrings[closest_index] if closest_index != float('inf') and closest_index != float('-inf') else ''