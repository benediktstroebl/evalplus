
def sorted_list_sum(lst):
    """Write a function that accepts a list of strings as a parameter,
    deletes the strings that have odd lengths from it,
    and returns the resulted list with a sorted order,
    The list is always a list of strings and never an array of numbers,
    and it may contain duplicates.
    The order of the list should be ascending by length of each word, and you
    should return the list sorted by that rule.
    If two words have the same length, sort the list alphabetically.
    The function should return a list of strings in sorted order.
    You may assume that all words will have the same length.
    For example:
    assert list_sort(["aa", "a", "aaa"]) => ["aa"]
    assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]
    """
    # initialize a variable to hold the sum of all elements in the list
    sum = 0
    # initialize a variable to hold the index of the next element to be added to the list
    index = 0
    # iterate through each element in the list
    for element in lst:
        # check if the length of the element is odd
        if len(element) % 2 == 1:
            # increment the sum and the index
            sum += element
            index += 1
        # if the length is odd, delete it from the list
        else:
            del lst[index]
            index -= 1
    # add the sum to the list
    lst.append(sum)
    # sort the list in ascending order by length of each word
    lst.sort(key=lambda x: x if isinstance(x, str) else int(x))
    return lst
