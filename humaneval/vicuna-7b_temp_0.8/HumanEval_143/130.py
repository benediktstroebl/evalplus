
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
    for word in words:
        if len(word) > 2:
            for i in range(2, len(word)):
                for j in range(i + 1, len(word)):
                    if (i + j) % 2 == 0:
                        continue
                    new_words.append(word[:i] + ' ' + word[i+1:] + ' ' + word[:j])
                    new_sentence = ' '.join(new_words)
                    if new_sentence == sentence:
                        return new_words[i]
    return ' '
