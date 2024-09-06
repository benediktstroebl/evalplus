

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """

    list1 = l1[:]
    list2 = l2[:]
    list1.sort()
    list2.sort()

    index = 0
    index_2 = 0

    common_list = []

    while True:
        try:
            current_element = list1[index]
            current_element_2 = list2[index_2]
            if current_element == current_element_2:
                common_list.append(current_element)

            if current_element > current_element_2:
                index_2 += 1
            else:
                index += 1

        except IndexError:
            break

    return sorted(set(common_list))

