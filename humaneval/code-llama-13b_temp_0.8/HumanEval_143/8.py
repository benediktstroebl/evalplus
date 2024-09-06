
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
    sentence_list = sentence.split()
    result = ""
    for word in sentence_list:
        word_length = len(word)
        prime_word = True
        for divisor in range(2, word_length):
            if word_length % divisor == 0:
                prime_word = False
                break
        if prime_word:
            result += word + " "
    return result.strip()

