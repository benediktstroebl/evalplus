
def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    words = S.split()
    return sum(1 for word in words if word=="I")

assert is_bored("Hello world") == 0
assert is_bored("The sky is blue. The sun is shining. I love this weather") == 1
assert is_bored("I love this weather") == 0
assert is_bored("I love this weather.") == 0
assert is_bored("I love this weather. It is sunny. The sun is shining. I'm bored.") == 1
assert is_bored("I love this weather. It is sunny. The sun is shining. I'm bored. There is also a plane flying over the clouds.") == 2
assert is_bored("I love this weather. It is sunny. The sun is shining. I'm bored. There is also a plane flying over the clouds.") == 2
assert is_bored("I love this weather. It is sunny. The sun is shining. I'm bored. There is also a plane flying over the clouds. There are also people on the dark side!") == 3
assert is_bored("Hello world. It is sunny. The sun is shining. I'm bored. There is also a plane flying over the clouds. There are also people on the dark side!.") == 0
assert is_bored("Hello world. It is sunny. The sun is shining. I'm bored. There is also a plane flying over the clouds. There are also people on the dark side!.") == 0
assert is_bored("Hello world. It is sunny. The sun is shining. I'm bored. There is also a plane flying over the clouds. There are also people on the dark side!.") == 0
assert is_bored("Hello world. It is sunny. The sun is shining. I'm bored. There is also a plane flying over the clouds. There are also people on the dark side!.") == 0
assert is_bored("Hello world. It is sunny. The sun is shining. I'm bored. There is also a plane flying over the clouds. There are also people on the dark side!.") == 0
assert is_bored("Hello world. It is sunny. The sun is shining. I'm bored. There is also a plane flying over the clouds. There are also people on the dark side!.") == 0
assert is_bored