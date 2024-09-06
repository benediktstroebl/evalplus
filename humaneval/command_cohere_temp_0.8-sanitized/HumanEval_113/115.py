def odd_count(strings):
    r = []
    for string in strings:
        if not string:
            r.append('the number of odd elements in the empty string of the input.')
        else:
            odd, even = 0, 0
            for char in string:
                if char % 2:
                    odd += 1
                else:
                    even += 1
            r.append(f'the number of odd elements in the string {odd} of the input.')
    return r