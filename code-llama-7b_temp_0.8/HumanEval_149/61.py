
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
    # The way I did this was with an if statement that if the length of the list was greater than 2,
    # then do what is inside the if statement, otherwise, return the original list.
    # I did this because if the list was smaller than 2, then I don't have to deal with the
    # sorting of the list.
    if len(lst) > 2:
        # I first converted the list into a set. This was because I was only going to need
        # unique values from the list, and if I had set, I would only need unique values.
        lst = list(set(lst))
        # I then created a new list, because I wanted to sort the list, which I could not do
        # with a set.
        new_lst = []
        # This was to help me deal with the sorting of the list.
        z = 0
        while z < len(lst):
            # I created a for loop to add the even lengthed strings into the new list.
            if len(lst[z]) % 2 == 0:
                new_lst.append(lst[z])
            z += 1
        # I then sorted the list in alphabetical order.
        new_lst.sort()
        # I returned the new list, in alphabetical order, of the even lengthed strings.
        return new_lst
    else:
        return lst

