
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_char_count = {}
    max_word = None
    max_word_idx = 0
    
    for word in words:
        word_len = len(word)
        
        if word not in max_char_count:
            max_char_count[word] = 1
        else:
            max_char_count[word] += 1
            
        if max_char_count[word] > max_char_count[max_char_count.get(max_word, 0)]:
            max_char_count[max_word] = max_char_count[word]
            max_word_idx = word_idx
            
    return max_word[::-1] if max_word_idx != 0 else max_char_count.get(max_char_count.most_common(max_word_idx)[0][0], "").lower()
