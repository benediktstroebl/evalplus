
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
    # Step 1: sort the list by length of words
    lst = sorted(lst)

    # Step 2: Create an empty list to store the sum
    sum_lst = []

    # Step 3: Loop through the sorted list
    for i in range(len(lst)):
        # Step 3.1: check if the current word is odd
        if lst[i].isdigit() == False:
            # Step 3.2: If not, append the current word to the sum list
            sum_lst.append(lst[i])
        else:
            # Step 3.3: If the current word is odd, append the previous word to the sum list
            sum_lst.append(lst[i-1])

    return sum_lst

print(list_sort(["aa", "a", "aaa", "bbb", "ccc", "aaa", "ddd"]))
