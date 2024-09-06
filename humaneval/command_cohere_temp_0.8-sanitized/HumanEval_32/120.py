import math
def find_zero(xs):
    """
    Finds a solution x for polynomial xs such that poly(x) = 0.
    Returns only the first found zero solution.
    Works only with lists xs having an even number of coefficients
    and the largest non-zero coefficient.
    """
    # Ensure xs has even length and largest coefficient is largest
    if len(xs) % 2 == 1:
        xs += [0]
    max_idx = xs.index(max(xs))
    xs[max_idx], xs[max_idx + 1] = xs[max_idx + 1], xs[max_idx]

    # Divide polynomial into pairs of coefficients
    # e.g. [1,2,3,4] => [(1,2), (3,4)]
    pairs = [(xs[i], xs[i + 1]) for i in range(0, len(xs), 2)]

    # Initialize xs values such that poly(x) = 0
    x = - xs[0] / xs[1]

    # Sort pairs by x^2 values
    sorted_pairs = sorted(pairs, key=lambda pair: math.pow(x, 2) * pair[0] + pair[1])

    # Update x to go through intervals
    while len(sorted_pairs) != 0:
        a, b = sorted_pairs.pop()
        x = (x + a / b) / (1 - a / b)

    # Return the x corresponding to the largest coefficient
    return x