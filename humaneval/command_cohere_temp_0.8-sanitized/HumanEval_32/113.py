import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for polynomial coefficients polynomial such that poly(x) = 0.
    Returns only one solution, even in the presence of multiple roots.
    Works only for lists coefficients with even number of elements
    and largest non-zero coefficient.
    """
    # Your code here, remove comments below
    # If there are no coefficients, return None
    if len(coefficients) == 0:
        return None

    # Filter out zero coefficients and get largest coefficient
    coefficients = [coeff for coeff in coefficients if coeff != 0]
    largest_coeff = max(coefficients)

    # Sort coefficients in descending order
    coefficients.sort(reverse=True)

    # Even number of coefficients
    if len(coefficients) % 2 == 0:
        x = (-largest_coeff) / (coefficients[0] / 2)
        return x

    # Odd number of coefficients
    else:
        # For degree 1, we have a single linear equation.
        # In this case, there will be two solutions,
        # we return the positive one (ignoring imaginary components)
        if len(coefficients) == 1:
            return abs(x)

        # Start with the solution for degree n - 1
        x = find_zero(coefficients[:-2])

        # Update solution with the last coefficient
        return adjust_solution(x, coefficients[-1])
def adjust_solution(x: float, coeff: float) -> float:
    """
    Adjust solution x by coefficient coeff
    return x if abs(x) >= coeff, return -x if x = coeff / 2
    return x * coeff if coeff < 0
    """
    abs_x = abs(x)
    if x == 0:
        return 0
    elif coeff >= abs_x:
        return x
    elif x == coeff / 2:
        return -x
    else:
        return x * coeff