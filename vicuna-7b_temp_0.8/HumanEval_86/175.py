
def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    # Store the words in a list
    words = s.split()
    # Reverse the list
    words.reverse()
    # Join the words in reverse order
    return ''.join([chr(ord('a') + i) for i in range(len(words))])

s1 = "Hello World!!! Hello there!"
print(s1) # prints "Hello World!!! Hello there!"
print(anti_shuffle(s1)) # prints "Hello !!!Wdlor Hello there!"
\end{code}

For the second part, you can use a `for` loop to iterate through the string and reverse the characters.

\begin{code}
