
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

    split_sentence = sentence.split()
    result = ""
    for word in split_sentence:
        if len(word) > 1:
            for i in range(1, len(word)):
                if word[i] == word[i-1] and int(word[i]) % 2 == 1 and int(word[i-1]) % 2 == 1:
                    result += word[i]
    return result
