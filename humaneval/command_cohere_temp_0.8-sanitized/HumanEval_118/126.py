def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that 
    stands between two consonants from the right side of the word."""
    
    # Ensure the word is lowercase
    word = word.lower()
    
    # Split the word into individual characters to simplify the process
    # and remove the unnecessary prefix and suffix vowel checks
    characters = list(word)
    
    # Initialize empty variables to store the closest vowel and its index
    closest_vowel = ""
    closest_vowel_index = 0
    
    # Loop through the right half of the characters
    for i in range(1, len(characters)):
        # Check if the current character is a consonant
        if characters[i].isalnum() and characters[i] != "y":
            # Check if the previous character is a vowel
            if (i > 0 and characters[i-1].isalnum() and 
                characters[i-1].lower() in ["a", "e", "i", "o", "u"]):
                # Check if the next character is a vowel
                if (i < len(characters)-1 and characters[i+1].isalnum() and
                    characters[i+1].lower() in ["a", "e", "i", "o", "u"]):
                
                    # If the above conditions are met, set the closest vowel 
                    # to the current character and its index, and break the loop
                    closest_vowel = characters[i]
                    closest_vowel_index = i
                    break
            else:
                # If the previous character isn't a vowel, set the current 
                # character as the closest vowel and its index, and break the loop
                closest_vowel = characters[i]
                closest_vowel_index = i
                break
    
    # Return the closest vowel or an empty string if no matching vowel is found
    return closest_vowel if closest_vowel != "" else ""