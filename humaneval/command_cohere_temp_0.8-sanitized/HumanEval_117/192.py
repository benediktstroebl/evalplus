def select_words(s, n):
    import re
    
    # Regex pattern to identify words and count consonants
    pattern = r'\b\w*?(?=(?:\b\w*?|\Z))'
    
    # Count consonants using regex
    def count_consonants(m):
        char_count = 0
        for c in m.group():
            if c in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
                char_count += 1
        return char_count
    
    words = re.findall(pattern, s)
    consonants_count = [re.sub(count_consonants, len, word) for word in words]
    
    return [word for i, word in enumerate(words) if consonants_count[i] == n]