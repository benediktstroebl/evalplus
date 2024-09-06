import math
def find_zero(xs):
    """
    Finds a solution x for the polynomial xs such that poly(x) = 0.
    Returns only the first solution x, even if there are multiple zeros.
    Works only for lists xs with an even number of coefficients, and the largest non-zero coefficient.
    """
    if len(xs) % 2 == 1 or max(xs) == 0:
        return "Invalid input. Input list must have an even number of coefficients and a non-zero largest element."

    # Substitute x with y - max(xs) to make the polynomial have a smaller largest coefficient and pivot it to the left
    xs_shifted = [y - max(xs) for y in xs]
    y_shifted = max(xs) - max(xs)

    # Reduce polynomial
    for _ in range(len(xs) // 2):
        xs_shifted.append(0)

    # Use synthetic division to divide the polynomial by (x-y_shifted)
    divisional_result = []
    for i, coeff in enumerate(xs_shifted):
        if i % 2 == 0:
            divisional_result.append(coeff)
        else:
            tmp = divisional_result.pop()
            divisional_result.append(tmp - coeff * y_shifted)

    # Extrapolate the solution from the divisional result
    solution_extrapolation = [math.nan, math.nan]
    for i in range(len(divisual_result)):
        solution_extrapolation.append(divisual_result[i] / divisional_result[i])

    solution_extrapolation.reverse()
    x_solution = solution_extrapolation[0]
    y_solution = solution_extrapolation[1]

    # If x_solution is not a valid number, the polynomial does not have a zero
    if math.isnan(x_solution):
        return "No valid solution found for the given polynomial."

    return x_solution, y_solution