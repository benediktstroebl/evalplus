import math
def find_zero(xs):
    """
    Finds a solution x for the polynomial xs such that poly(x) = 0.
    Only returns the first solution found.
    Guarantees a solution only if there are an even number of coefficients in xs
    and the largest non-zero coefficient is passed.
    """
    if len(xs) % 2 == 0:
        # Assuming xs is sorted
        # ex. [1, 2, 4, 6] -> [1, 2, 1, 2] -> [1, 1] -> 0
        #      [1, -2, 3, -4] -> [1, -2, 1, -2] -> [1, 0] -> 0
        xs = xs[1:-1]
        # Find the middle coefficient index where repetitions occur
        # ex. [1, 2, 4, 6] -> 2, [1, -2, 3, -4] -> 3
        middle_index = len(xs) // 2
        # Divide the polynomial into quadratic parts
        # ex. [1, 2, 4, 6] -> ([1, 2], [2, 4], [4, 6])
        xs = [xs[:middle_index], xs[middle_index:middle_index*2], xs[middle_index*2:]]
        # Determine signs for each part
        # ex. ([1, 2], [2, 4], [4, 6]) -> (1, -1, 1)
        signs = [1 if xs[0] > 0 else -1,
                 -1 if xs[0] < 0 else 1,
                 1 if xs[-1] > 0 else -1]
        # Determine the middle coefficient for each part
        # ex. ([1, 2], [2, 4], [4, 6]) -> (2, 2, 4)
        middles = [xs[len(xs) // 2], xs[len(xs) // 4], xs[len(xs) // 2 * 2]]
        # Calculate discriminants for each part
        # ex. (1, 2, 4) -> (4, 0, 4)
        discriminants = [m * m * s for m, s in zip(middles, signs)]
        # Find the solution in each part
        # ex. (4, 0, 4) -> (0, 2, 2)
        solutions = [math.sqrt(discriminant) for discriminant in discriminants]
        # Return the first solution
        return solutions[0]
    else:
        raise ValueError("must be an even number of coefficients")