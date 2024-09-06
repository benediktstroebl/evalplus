
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
    for i in range(1, len(words)):
        for j in range(i+1, len(words)):
            if words[i] in words[j]:
                if len(words[i]) % 2 != 0 or len(words[j]) % 2 != 0:
                    words[i], words[j] = words[j], words[i]
                break
    return ' '.join(words)