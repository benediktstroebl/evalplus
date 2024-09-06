
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
    result = []
    i = 0
    while i < len(words) - 1:
        while not all(x % 1 == y for x, y in zip(words[i:i+2], words[i+1:i+3])):
            i += 1
        result.append(words[i])
        i += 1
    result.append(words[i])
    return ' '.join(result)