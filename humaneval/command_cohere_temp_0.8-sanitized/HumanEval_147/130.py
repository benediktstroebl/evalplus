def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n + 1)]
    
    # Calculate the maximum triples
    triples = 0
    for i in range(n):
        for j in range(i + 1, n):
            curr = a[i] + a[j]
            if curr % 3 == 0:
                triples += 1
            elif curr % 3 == 1:
                # Subtract occurrences of curr as both pairs (a[i], a[j]) and (a[j], a[k]) are counted
                triples -= occurrences_of(curr, a)
            elif curr % 3 == 2:
                # Add occurrences of curr as both pairs (a[i], a[j]) and (a[j], a[k]) are counted
                triples += occurrences_of(curr, a)
    
    return triples
def occurrences_of(number, lst):
    # Count the occurrences of a number in a list
    return sum(1 for i in lst if i == number)