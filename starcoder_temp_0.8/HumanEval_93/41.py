
def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    answer = ''
    for i in message:
        if i in vowel_list:
            if i == 'a':
                answer += 'a'
            else:
                answer += vowel_list[(vowel_list.index(i)+2)%5]
        elif i.isupper():
            answer += i.lower()
        else:
            answer += i.upper()
    return answer
