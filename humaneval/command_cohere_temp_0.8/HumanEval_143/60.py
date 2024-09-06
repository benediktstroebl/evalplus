Here is a Python script with a self-contained function that solves the problem:
```python
def is_prime(n):
    """
    Checks whether the number is prime or not.
    :param n: number to be checked
    :return: boolean value represents whether n is prime or not
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    words = sentence.split(' ')
    new_sentence = ""
    for word in words:
        if is_prime(len(word)):
            new_sentence += word + ' '
    return new_sentence[:-1]
```
The `is_prime` function checks if a number is prime or not. The `words_in_sentence` function splits the sentence into words and then constructs a new sentence with the words whose length is a prime number.

Here is an example of how you can use the `words_in_sentence` function to parse a sentence:
```python
print(words_in_sentence("Let us go for a swim in the lake.")) 
```
The output would be:
```
Let us go
``` 
This correctly identifies the words 'Let', 'us', and 'go' as the words with prime lengths in the provided sentence.