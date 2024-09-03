def select_words(s, n): 
    # Remove all characters except a vowel and number 
    s= [c for c in s if c.isalpha('a') or string.isdigit(c)]

    # Filter and return the words that have n consonants 
    return [word for word in s if word.count('c') == n]