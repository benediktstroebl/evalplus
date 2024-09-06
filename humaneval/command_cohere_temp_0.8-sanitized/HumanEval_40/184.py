def triples_sum_to_zero(lst):
    # Calculate total sum and count of items
    total_sum = sum(lst)
    item_count = len(lst)

    # Verify if there are three items whose sum is zero
    for a in lst:
        if total_sum - a == 0 and item_count - 2 == 0:
            return True
        if total_sum - a == 0 and item_count - 2 > 0:
            continue
        if a == 0 and item_count - 3 == 0:
            return True
        if a == 0 and item_count - 3 > 0:
            continue

    return False