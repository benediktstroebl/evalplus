def tri(n):
    if n == 0:
        return []
    if n == 1:
        return [1]
    list_of_trib = [0, 1, 3]
    if n % 2 == 0:
        return list_of_trib + [tri(n - 1)]
    else:
        return list_of_trib + [tri(n - 1) + tri(n - 2) + tri(n + 1)]