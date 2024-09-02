
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
    sentence = sentence.split()
    result = ''
    for word in sentence:
        is_prime = True
        if len(word) > 1:
            for i in range(2, len(word)):
                if (word[0] == word[i]) and (word[1] == word[i]):
                    is_prime = False
                    break
        else:
            is_prime = False
        if is_prime:
            result += word + ' '
    return result[:-1]
