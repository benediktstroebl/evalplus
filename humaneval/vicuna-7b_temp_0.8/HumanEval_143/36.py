
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
    new_words = []
    for word in words:
        if len(word) > 2:
            new_words.append(word)
    for i in range(len(new_words)):
        for j in range(i+1, len(new_words)):
            if new_words[i] < new_words[j]:
                j = j + 1
            if (new_words[i] % j) != 0:
                new_words[i], new_words[j] = new_words[j], new_words[i]
                break
    return ' '.join(new_words)

sentence = input().lower()
