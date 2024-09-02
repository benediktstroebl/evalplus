
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
    words = sentence.split()
    words = [x for x in words if len(x) > 2]
    words.sort(key=lambda x: 10**(int(x.count('0'))))
    new_sentence = ''
    for i, x in enumerate(words):
        if i == 0 or i == 1:
            continue
        if len(x) % 2 == 0:
            continue
        new_sentence += x
    return new_sentence