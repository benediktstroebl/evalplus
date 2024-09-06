
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
    sentence = sentence.lower()
    words = sentence.split()
    prime_words = []
    for word in words:
        if len(word) % 1 == 0:
            prime_words.append(word)
        else:
            prime_words.append("*")
    prime_words = ' '.join(prime_words)
    return prime_words

input = "This is a test"
print(words_in_sentence(input))
input = "lets go for swimming"
print(words_in_sentence(input))
