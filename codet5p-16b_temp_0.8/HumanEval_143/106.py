
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

    result = ""
    for word in sentence.split(' '):
        if len(word) > 0:
            if len(word) == 2: # the word is two letters long
                for w in word:
                    result += w
            elif len(word) > 2:
                result += word[0]
                for i in range(1, len(word)):
                    if is_prime(i):
                        result += word[i]
                if len(word) > 2:
                    result += word[-1]
    return result

