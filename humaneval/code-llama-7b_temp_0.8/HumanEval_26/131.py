from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # === Slides 101-102 ===
    # === Step 1 ===
    # create a list of items and their number of occurrences
    item_to_occurrence = {}
    for item in numbers:
        if item in item_to_occurrence:
            item_to_occurrence[item] += 1
        else:
            item_to_occurrence[item] = 1

    # === Step 2 ===
    # create a list of items to keep and delete
    items_to_keep = []
    items_to_delete = []
    for item, occurrence in item_to_occurrence.items():
        if occurrence == 1:
            items_to_keep.append(item)
        else:
            items_to_delete.append(item)

    # === Step 3 ===
    # make a list to return
    result = []
    for item in items_to_keep:
        result.append(item)

    return result

