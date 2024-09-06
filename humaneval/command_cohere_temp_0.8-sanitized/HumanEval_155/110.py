def even_odd_count(num):
    if isinstance(num, int):
        # Remove non-digit characters from input (if any)
        num = str(num).strip('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        return (len(list(filter(lambda x: x % 2 == 0, num))), len(num))
    else:
        raise TypeError("Input must be an integer")