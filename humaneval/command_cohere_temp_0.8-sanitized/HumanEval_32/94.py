import math
def find_zero(xs: list) -> float:
    """
    xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    # Check if the input list has 2*n elements and all elements are numbers
    if len(xs) % 2 == 0: 
        # Check if the list has any non-numeric elements
        for x in xs:
            if not isinstance(x, (int, float)): 
                print('Warning: ignoring non-numeric element')
                return None
        # Sort list in increasing order 
        xs.sort(key=lambda x: abs(x))
        # Number of zeros depends on the leading coefficient's sign
        if xs[0] > 0: 
            return -xs[::-1][0] / (xs[1:] + [0]*(len(xs)-2))[0]
        elif xs[0] < 0: 
            return xs[0] / (xs[1:] + [0]*(len(xs)-2))[0]
        else: 
            return 0  
    return None