def words_in_sentence(sentence):
    sentence = sentence.split()
    words = []
    for word in sentence:
        if len(word) > 1 and len(word) in prime_numbers:
            words.append(word)
    return ' '.join(words)
prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]