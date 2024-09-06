def select_words(s, n):
    """
    Find words in a string that contain a certain number of consonants.
    """
    def count_consonants(word):
        c = 0
        for letter in word:
            if letter in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
                c += 1
        return c
    
    words = [word.strip() for word in s.split(' ') if word.strip()]
    result = [word for word in words if count_consonants(word) == n]
    return result