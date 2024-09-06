def cycpattern_check(first, second):
    return second in set(word for word in (second, *second[1:], second[1:0]) if word in first)