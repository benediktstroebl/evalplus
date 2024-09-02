
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
    # Step 1: Check if the list is empty
    if not lst:
        return []
    
    # Step 2: Create an empty list to store the result
    result = []
    
    # Step 3: Add the first string in the list to the result list
    result.append(lst[0])
    
    # Step 4: Sort the remaining elements in the list and add them to the result
    sorted_list = sorted(lst[1:], key=lambda x: len(x))
    result.extend(sorted_list)
    
    # Step 5: Remove any strings with odd lengths from the result
    result = [x for x in result if len(x) % 2 == 0]
    
    return result
