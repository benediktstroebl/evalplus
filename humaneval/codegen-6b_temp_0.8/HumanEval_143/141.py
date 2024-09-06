
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
    from collections import OrderedDict
    words = sentence.split(' ')

    new_words = []

    for word in words:
        if len(word) == 1:
            new_words.append(word)
        else:
            p = 2
            while p < len(word):
                if len(word) % p != 0:
                    p += 1
                else:
                    break

            modified_word = word[0:p]

            if ord(modified_word[0]) > 122:
                modified_word = modified_word.lower()

            new_words.append(modified_word)

    new_words = OrderedDict.fromkeys(new_words).keys()

    return ' '.join(new_words)

