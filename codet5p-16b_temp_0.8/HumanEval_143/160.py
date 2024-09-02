
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
    words = re.split('\s+', sentence)
    res = []
    for word in words:
        if len(word) > 1 and word[0] in 'bcdfghjklmnpqrstvwxyz':
            if len(word) == 2:
                if len(word) in [3, 5, 7, 11, 13, 17, 19, 23, 29]:
                    res.append(word)
            elif len(word) % 2 == 0:
                if len(word) in [3, 7, 11, 13, 17, 19, 23, 29]:
                    res.append(word)
            else:
                if len(word) in [5, 7, 11, 13, 17, 19, 23, 29]:
                    res.append(word)
    return''.join(res)

