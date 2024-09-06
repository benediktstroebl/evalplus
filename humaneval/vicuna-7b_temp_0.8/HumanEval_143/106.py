
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
    sentence = sentence.upper()
    n = len(sentence)
    words = sentence.split()
    result = []
    for i in range(n):
        for j in range(i + 1, n):
            if len(words[i]) % len(words[j]) == 0:
                result.append(words[i])
                break
        else:
            result.append(words[i])
    return " ".join(result)