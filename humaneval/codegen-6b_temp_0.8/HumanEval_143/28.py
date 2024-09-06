
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
    # empty sentence
    if sentence == "":
        return ""

    # create a set of all letters
    letters = set()
    for letter in sentence:
        letters.add(letter)
    print(letters)

    all_words = [word for word in sentence.split() if word not in letters]
    print(all_words)

    all_words.sort(key=len)
    print(all_words)
    return "".join(all_words)

