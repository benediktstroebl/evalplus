def largest_smallest_integers(lst):
    positive = float('-inf')
    negative = float('inf')
    for n in lst:
        if n > 0:
            positive = min(positive, n)
        else:
            negative = max(negative, n)
    return (negative if negative != float('inf') else None,
            positive if positive != float('-inf') else None)