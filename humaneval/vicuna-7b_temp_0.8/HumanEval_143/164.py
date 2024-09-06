
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
    words_lengths = [len(word) for word in words]
    prime_words = []
    for i in range(len(words_lengths)):
        words_lengths[i] = [x for x in xrange(1, len(words_lengths[i]) + 1) if x % 2 == 0]
    for i in xrange(len(words_lengths)):
        if words_lengths[i] == 1:
            prime_words.append(words[i])
        else:
            prime_words.append("".join([words[i*2], words[i*2+1]]))
    return " ".join(prime_words)

