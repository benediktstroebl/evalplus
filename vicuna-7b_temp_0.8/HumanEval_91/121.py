
def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
    
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    # Use a dictionary to store the count of boredoms
    boredoms_count = {word: 0 for word in S}
    
    # For each character in the string
    for char in S:
        # If the character is a letter
        if char.isalpha():
            # If the character is a vowel
            if char in "aeiou":
                # Increment the count of boredoms
                boredoms_count[char] += 1
            elif char == "i":
                # If the word before the character is a boredom
                if boredoms_count[char-1] != 0:
                    boredoms_count[char] += 1
    
    # Return the count of boredoms
    return boredoms_count
