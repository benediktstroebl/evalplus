
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
    i = 0
    while i < len(words) - 1:
        word = words[i]
        for j in range(i + 1, len(words)):
            if not word or not words[j]:
                break
            if word.isdigit():
                continue
            if word.isalpha() and len(word) > 1:
                new_words.append(word)
                i += 1
            else:
                new_words.append("".join(reversed(words[i].split())))
                i += 1
    return "".join(new_words)
