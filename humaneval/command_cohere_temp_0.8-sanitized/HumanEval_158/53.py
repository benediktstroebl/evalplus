def find_max(words):
    char_count = {}
    max_word = None
    for word in words:
        unique_chars = set(word)
        if len(unique_chars) > len(char_count):
            char_count = unique_Chars
            max_word = word
        elif len(unique_chars) == len(char_count):
            for char in word:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
    
    return max_word