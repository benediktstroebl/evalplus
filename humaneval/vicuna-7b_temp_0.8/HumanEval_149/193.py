
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
    # Step 1: Create an empty list to store the sorted strings
    sorted_list = []

    # Step 2: Create a new list that contains all the words in the original list,
    # but only the words that have an even number of letters
    even_list = [x for x in lst if len(x) % 2 == 0]

    # Step 3: Add the sorted strings to the sorted_list list
    for x in even_list:
        sorted_list.append(x)

    # Step 4: Add the missing elements to the sorted_list list
    for y in lst:
        if len(y) % 2 != 0:
            sorted_list.append(y)

    # Step 5: Sort the sorted_list list
    sorted_list.sort()

    return sorted_list
