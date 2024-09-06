
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
    if sentence is None or len(sentence) == 0:
        return sentence
    sentence = sentence.split(" ")
    new_list = []
    for word in sentence:
        word = [w for w in word]
        for idx, w in enumerate(word):
            if idx == 0 or idx == len(word) - 1:
                continue
            if w != w.lower() and w != w.upper():
                word[idx] = " "
        word = "".join(word)
        if is_prime(len(word)):
            new_list.append(word)
    return " ".join(new_list)

