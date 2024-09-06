

def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """

    # This solution is a bit complicated, but we're not just solving
    # the problem, we're also trying to demonstrate a technique we
    # can use to debug the solution.
    #
    # The technique is to use assert statements to make sure our code
    # is working as expected. 
    #
    # It is easy to say that the words are not the same if they
    # are not the same length.
    if len(s0) != len(s1):
        # If we get here, we've already determined they're not the same.
        # We can return False immediately.
        return False

    # Next we want to determine if the characters in s0 are all in s1
    # and if the characters in s1 are all in s0.
    #
    # One way to do this is to loop through the characters in s0
    # and check if they're in s1.  Then we loop through the characters
    # in s1 and check if they're in s0.
    #
    # But that has a lot of looping.  What if we could do it in a single
    # pass?  What if we could remove the characters from s1 as we go,
    # and then check if s1 is empty?

    # Since we're going to remove characters, we need to make a copy
    # of s1 so we don't modify the original.
    #
    # When we modify a variable (like s1), we have to be careful.
    # In this case, we're changing the contents of s1.  If we do this,
    # the second loop will fail.  So we have to make a copy.
    s1_copy = s1[:]

    # Since we know the two strings are the same length, we can just loop
    # through the first string and remove characters from s1_copy.
    #
    # We can use a for loop to loop through the string, but we can't just
    # loop through the characters in the string.  Strings are immutable
    # (they can't be changed), so we need to loop through the indices.
    for i in range(len(s0)):
       
