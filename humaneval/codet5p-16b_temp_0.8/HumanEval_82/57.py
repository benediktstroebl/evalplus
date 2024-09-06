
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    l = [int(x) for x in string]
    l = list(set(l))
    l.sort()
    if len(l) == 1:
        return True
    else:
        i = 0
        while i < len(l):
            j = i + 1
            while j < len(l):
                if l[i] == l[j]:
                    return False
                else:
                    if (l[i] + l[j]) in l:
                        return False
                j += 1
            i += 1
    return True

