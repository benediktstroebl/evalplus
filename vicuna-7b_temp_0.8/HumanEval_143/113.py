
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
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if words[i] == " " or words[j] == " ":
                continue
            if not(is_prime(len(words[i])) or is_prime(len(words[j]))):
                words[i:j] = [word for word in words[i:j] if word.islower() and is_prime(len(word))]
            elif len(words[i]) != len(words[j]):
                words[i:j] = [word for word in words[i:j] if word.islower() and is_prime(len(word)) and len(words[i]) != len(words[j])]
        words[i:]=[" "]

    return " ".join(words)