Here's a Python script that solves the given problem with an example:
```python
def is_prime(n):
    """
    Checks whether the number is prime or not.

    Args:
        n (int): Number to check if prime

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Args:
        sentence (str): A string representing a sentence with words separated by spaces.

    Returns:
        str: A string containing words whose lengths are prime numbers.
    """
    words = sentence.split(" ")
    result = []
    for word in words:
        if is_prime(len(word)):
            result.append(word)
    return " ".join(result)

# Example usage
sentence = "This is a test"
print(words_in_sentence(sentence))  # Output: "is"
```

In the above code, the `is_prime` function checks whether a number is prime or not, and the `words_in_sentence` function splits the input sentence into words and then checks the length of each word, appending the prime-length-word to the result list. Finally, the function joins the resulting list of prime words to form a string.