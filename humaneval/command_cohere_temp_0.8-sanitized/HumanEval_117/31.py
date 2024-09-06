def select_words(s, n):
    def find_words(s, target, count):
        if not s:
            if target == count:
                return [s]
            return []
        if s[0].isalpha():
            consonant_word = find_words(s[1:], target, count) + [s[:1].lower()]
            return consonant_word + find_words(s[1:], target, count-1)
        else: 
            return find_words(s[1:], target, count)
    
    words = [word for word in s.split()]
    return find_words("", words, n)