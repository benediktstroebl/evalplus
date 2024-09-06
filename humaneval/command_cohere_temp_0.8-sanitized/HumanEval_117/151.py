def select_words(s, n):
    """
    Find words in a string that contain exactly n consonants.
    
    Args:
        s (str): Input string.
        n (int): Number of consonants required in each word.
        
    Returns:
        list: List of words containing exactly n consonants.
    """
    # Ensure the input is not empty and the number of consonants is a positive integer
    if not s or not n or n > len(s) or n > 26:
        return []

    # Use a dictionary to keep track of consonants encountered for each index
    consonant_counts = [0] * (len(s) + 1)
    vowels = 'AEIOUaeiou'
    for char in s:
        if char.isalpha():
            index = s.index(char)
            if char in vowels:
                consonant_counts[index] += -1
            else:
                consonant_counts[index] += 1

    # Find the indices where the total count of consonants in the dictionary is n
    candidates = [i for i, count in enumerate(consonant_counts) if count == n]

    # Filter out non-letter boundaries and invalid candidates
    words = []
    start = 0
    while candidates:
        end = candidates.pop()
        if start < end:
            words.append(s[start:end])
        start = end + 1  # Increment the start position for the next word

    return words