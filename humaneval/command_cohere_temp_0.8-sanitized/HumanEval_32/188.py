import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the polynomial equation poly(x) = 0.
    Returns x such that poly(x) = 0 for the given polynomial with coefficients coefficients.
    Guarantees a solution for lists with an even number of coefficients.
    """
    # Check that list has even number of coefficients and a largest non-zero coefficient
    if len(coefficients) % 2 == 1 or coefficients[-1] == 0:
        return "Invalid input for polynomial coefficients."

    # Partition list into pairs of coefficients
    x_pairs = [coefficients[i:i+2] for i in range(0, len(coefficients), 2)]
    
    # Try each pair of coefficients (c1, c2) with equation c1*x+c2*x^2 = 0
    for c1, c2 in x_pairs:
        # Calculate root using quadratic formula for equation c1x^2 + c2x + 0 = 0
        root1 = math.sqrt(-c2 / c1)
        root2 = root1 * math.sqrt(-c2 / c1)
        if root1 > 0 and root2 > 0:
            return root1
        elif root1 < 0 and root2 < 0:
            return root2
        elif root1 <= 0 and root2 >= 0:
            return root2
        elif root1 >= 0 and root2 <= 0:
            return root1