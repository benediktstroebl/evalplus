Here's a Python script that contains a function called `words_in_sentence` that solves the problem you've described:
```python
def is_prime(n):
    """
    Checks if a number is prime or not.

    Args:
        n (int): Number to check if it is prime

    Returns:
        bool: True if n is prime, False otherwise
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
        sentence (str): A string representing a sentence with space-separated words.

    Returns:
        str: A string containing words with prime lengths from the original sentence.

    Example:
        Input: sentence = "This is a test"
        Output: "is"
    """

    words = sentence.split()  # Split the sentence into words using space as separator
    prime_words = []            # List to store prime words

    for word in words:
        if is_prime(len(word)):  # Check if the length of the word is prime
            prime_words.append(word)  # Add the word to the list if it's prime

    return ' '.join(prime_words)  # Join prime words to form a string and return

# Example usage
sentence = "This is a test"
result = words_in_sentence(sentence)
print(result)  # Output: "is"
```

The provided example usage demonstrates how to call the function and print the expected output. The `is_prime` function is also included and detailed within the code, it is used to determine whether a given number is prime.

You can add more test cases in the same file to thoroughly test the function under various scenarios. Feel free to ask any questions or share additional ideas to improve this solution.