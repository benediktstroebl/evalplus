import math
def find_zero(xs: list) -> float:
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    # Check for curve with only one node
    if (len(xs) == 2 and xs[0] == 0 and xs[1] == 0):
        return 0

    # Check for vertical line
    if (len(xs) == 2 and xs[0] == 0):
        return xs[1]

    # Even number of coefficients
    if (len(xs) % 2 != 0):
        print("List xs should have even number of coefficients")
        return None

    # Take absolute values of xs
    xs = [abs(x) for x in xs]

    # Sort xs in descending order
    xs.sort(reverse=True)

    # Number of zeros could be 2*nds - 1, nds = floor((n+1)/2)
    nds = (len(xs)+1)//2
    zeros = []

    for i in range(nds):
        # calculating corresponding x for ith zero
        x = -xs[i] / (2*i + 1)
        zeros.append(x)

    # Here we are after all possible zeros,
    # now we find the only one find_zero function guarantees
    # It is the middle point between the smallest zero and the second smallest zero
    return (zeros[0] + zeros[1])/2