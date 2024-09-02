
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
    new_sentence = ""
    for word in words:
        if len(word) > 1:
            new_sentence += word
        else:
            new_sentence += " "
    for i in range(1, len(new_sentence)):
        if new_sentence[i] == " ":
            new_sentence = new_sentence[:i] + new_sentence[i+1:]
            break
    new_sentence = new_sentence.strip()
    prime_words = [word for word in words if len(word) == i and word.isdigit()]
    return new_sentence.join(prime_words)
