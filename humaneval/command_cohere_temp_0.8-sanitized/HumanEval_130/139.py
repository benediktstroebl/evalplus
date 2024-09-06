def tri(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    list_of_trib = [0] * (n + 1)
    list_of_trib[0] = 1
    list_of_trib[1] = 3
    for i in range(2, n + 1):
        if i % 2 == 0:
            list_of_trib[i] = 1 + i // 2
        else:
            list_of_trib[i] = list_of_trib[i - 1] + list_of_trib[i - 2] + list_of_trib[i + 1]
    return list_of_trib