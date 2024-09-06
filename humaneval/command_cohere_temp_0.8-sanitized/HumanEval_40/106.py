def triples_sum_to_zero(lst):
    # Define the variable to store whether a triple is found
    found = False

    # Iterate through the list
    for i in range(len(lst)):
        for j in range(i + 1):
            for k in range(j + 1):
                if lst[i] + lst[j] + lst[k] == 0:
                    found = True
                    break

            if found:
                break

    return found