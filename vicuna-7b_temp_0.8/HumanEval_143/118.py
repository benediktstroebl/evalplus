
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
    words = sentence.split()
    new_words = []
    for word in words:
        if len(word) > 1:
            new_words.append(word)
    while len(new_words) > 0:
        curr_word = new_words.pop()
        new_words.append(curr_word)
        for i in range(1, len(curr_word)):
            for j in range(i + 1, len(curr_word)):
                if curr_word[i:j] == curr_word[i:j] % 2 and curr_word[i:j] % 2 != 0:
                    new_words.append(curr_word[i:j])
                    break
    return " ".join(new_words)