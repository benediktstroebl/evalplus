
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if len(string) == 1:
        return True
    else:
        list = []
        for x in string:
            list.append(x)
    list.sort()
    n = len(list)
    for i in xrange(n):
        if i == 0:
            continue
        else:
            if len(list[i]) > 1:
                if len(list[i]) % 2 == 0:
                    if len(list[i]) == 2:
                        list.remove(list[i])
                    if len(list[i]) == 3:
                        list.remove(list[i])
                    if len(list[i]) > 3:
                        if list[i][0] == list[i][-1]:
                            list.remove(list[i])
                        else:
                            continue
                if len(list[i]) % 3 == 0:
                    if len(list[i]) == 3:
                        list.remove(list[i])
                    if len(list[i]) == 4:
                        list.remove(list[i])
                    if len(list[i]) > 4:
                        if list[i][0] == list[i][-1]:
                            list.remove(list[i])
                        else:
                            continue
                if len(list[i]) % 5 == 0:
                    if len(list[i]) == 5:
                        list.remove(list[i])
                    if len(list[i]) == 6:
                        list.remove(list[i])
                    if len(list[i]) > 6:
                        if list[i][0] == list[i][-1]:
                            list.remove(list[i])
                        else:
                            continue
                if len(list[i]) % 7 == 0:
                    if len(list[i]) == 7:
                        list.remove(list[i])
                    if len(list[i]) == 8:
                        list.remove(list[i])
                    if len(list[i]) > 8:
                        if list[i][0] == list[i][-1]:
                            list.remove(list[i])
                        else:
                            continue
                if len(list[i])