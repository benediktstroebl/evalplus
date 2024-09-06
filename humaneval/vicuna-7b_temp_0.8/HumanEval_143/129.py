
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
    words = [word for word in words if len(word) > 0]
    words = sorted(words)
    length_list = [len(word) for word in words]
    length_list = sorted(length_list)
    new_words = []
    while len(length_list) > 0:
        length = length_list[-1]
        if length % 2 != 0:
            new_words.append(length_list.pop(0))
        else:
            new_words.append(words[0])
    return ' '.join(new_words)
