
FIX = """
Add more test cases.
"""

def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """

    # your code goes here
    a=0
    b=0
    c=0
    d=0
    e=0
    # write your code here
    for x in s:
        if x=='a' or x=='A':
            a+=1
        if x=='e' or x=='E':
            e+=1
        if x=='i' or x=='I':
            i+=1
        if x=='o' or x=='O':
            o+=1
        if x=='u' or x=='U':
            u+=1
        if x=='y' or x=='Y':
            y+=1

    return a+e+i+o+u+y
