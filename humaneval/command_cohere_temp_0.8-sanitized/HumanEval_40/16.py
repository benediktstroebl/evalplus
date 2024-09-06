def triples_sum_to_zero(lst):
    # Initialize a counter to count the number of items in the list with certain values
    counter = Counter(lst)
    # Check if there are any values with a count divisible by three
    for num, count in counter.items():
        if count % 3 == 0:
            return True
    return False