
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

    import re

    sentence = sentence.split(' ')
    for word in sentence:
        if len(word) <= 1:
            return sentence
    new_sentence = []
    for word in sentence:
        if len(word) >= 2:
            new_sentence.append(word[0] + str(len(re.findall(r'\d+', word)))) + word[1:]
    return''.join(new_sentence)
