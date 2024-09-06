
def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """
    sentence_length = len(sentence)
    valid_words = []
    for length in range(2, sentence_length):
        for index in range(sentence_length - length + 1):
            word = sentence[index: index + length]
            if is_prime(length) and word.find(' ') == -1:
                valid_words.append(word)
    return ' '.join(valid_words)

