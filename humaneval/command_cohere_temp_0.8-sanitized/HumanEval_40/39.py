def triples_sum_to_zero(lst):
    # Calculate total sum and count of items
    total_sum = sum(lst)
    num_items = len(lst)

    # Check if there are three distinct elements that sum to zero
    for a in lst:
        if total_sum - a == 0 and lst.count(a) == 1:
            return True

    # If we reached this point, there are no such triplets
    return False