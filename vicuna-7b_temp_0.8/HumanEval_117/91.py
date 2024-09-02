
def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    """
    # Use a stack to keep track of the last consonants encountered
    stack = []
    # Use a queue to hold the current word and its index
    queue = []
    # Iterate through the string
    for i in range(len(s)):
        # If the current character is a consonant, push it on the stack
        if s[i] in 'bcdfghjklmnpqrstvwxyz':
            stack.append(s[i])
        # If the current character is a vowel or the end of the string
        elif s[i] in 'aeiouAEIOU':
            stack.pop()
            # If the stack is empty, check if the queue is empty
            if not stack:
                if not queue:
                    return []
                # Otherwise, check if the word at the head of the queue has the
                # same starting consonants as the last word in the stack
                if queue[-1][:len(stack)] == stack:
                    # Remove the word at the head of the queue and add its tail
                    # to the front of the queue
                    queue.pop(0)
                    queue.append(queue.pop(0))
                    # If the stack is empty, return the word at the head of the queue
                    if not stack:
                        return [queue[0]]
    return []
