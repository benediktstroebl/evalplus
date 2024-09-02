
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
    length_of_words = [len(word) for word in words]
    for i in range(1, len(length_of_words)):
        if not all(x % i for x in length_of_words[i]):
            words = [word for word in words if x % i == 0 for x in length_of_words]
            break
    return ' '.join(words)